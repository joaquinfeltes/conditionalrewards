# EL ALGORITMO QUE TENGO QUE HACER ES EL QUE RESUELVE LAS BELLMAN EQUATIONS (CREO)

# voy a hacer la clase del juego estocastico, una clase para cada nodo
import numpy as np
import random
from Reverse_DFS import reverse_dfs

PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"
PROBABILISTIC = "Probabilistic"


class StochasticGame:
    """A stochastic game, with two players,
    a reward list, a set of final states and a transition matrix. All rewards are positive."""

    def __init__(self, reward_list, transition_matrix, final_states):
        self.num_states = len(reward_list)
        self.reward_list = reward_list
        self.final_states = final_states
        self.transition_matrix = transition_matrix

    def init_states(self):
        state_list = [None] * self.num_states

        for state_n, transitions in enumerate(self.transition_matrix[0]):
            if transitions:
                state_list[state_n] = PlayerNode(
                    player=PLAYER_1, current_state=state_n, next_states=transitions, reward=self.reward_list[state_n])

        for state_n, transitions in enumerate(self.transition_matrix[1]):
            if transitions:
                state_list[state_n] = PlayerNode(
                    player=PLAYER_2, current_state=state_n, next_states=transitions, reward=self.reward_list[state_n])

        for state_n, transitions in enumerate(self.transition_matrix[2]):
            if transitions:
                state_list[state_n] = ProbabilisticNode(
                    player=PROBABILISTIC, current_state=state_n,
                    next_states=transitions, reward=0, is_final_node=(state_n in self.final_states))

        if None in state_list:
            idx = state_list.index(None)
            raise ValueError(f"Transition for state {idx} is not defined")
        return state_list

    def _set_game_for_reachability(self, state_list):
        state_list_for_reachability = []
        for state in state_list:
            state_for_reachabiliy = state.set_node_for_reachabily()
            state_list_for_reachability.append(state_for_reachabiliy)
        return state_list_for_reachability

    def solve_reachability(self, state_list):
        state_list = self._set_game_for_reachability(state_list)
        reachability_strategies = Solver.solve_reachability(state_list, self.transition_matrix, self.final_states)
        return reachability_strategies

    def solve_total_rewards(self, state_list, reachability_strategies):
        final_strategies = Solver.solve_total_rewards(state_list, self.transition_matrix, reachability_strategies)
        return final_strategies

    def solve(self):
        state_list = self.init_states()
        reachability_strategies = self.solve_reachability(state_list)
        final_strategies = self.solve_total_rewards(state_list, reachability_strategies)
        return final_strategies


class Node:
    """The base node class
    current_state: a str, is the name of the current state
    next_states: a list of tuples, every tuple contains the next state and an action or a probability
    """

    def __init__(self, player, current_state, reward, next_states):
        self.player = player
        self.current_state = current_state
        self.reward = reward
        self.next_states = next_states
        self.is_final_node_ = False
        self.reach_probability = 0


class ProbabilisticNode(Node):
    def __init__(self, current_state, reward, next_states, is_final_node=False):
        super().__init__(current_state, reward, next_states)
        self.is_loop_node = self._is_loop_node()
        self.is_final_node_ = is_final_node

    def _is_loop_node(self):
        return len(self.next_states) == 1 and self.current_state == self.next_states[0]

    def get_next_state(self):
        next_states, probabilities = zip(*next_states)
        # random.choices returns a list with one element
        return random.choices(next_states, probabilities)[0]

    def set_node_for_reachabily(self):
        reward = 1 if self.is_final_node else 0
        return ProbabilisticNode(self.current_state, reward, self.next_states)


class PlayerNode(Node):
    def __init_(self, player, current_state, reward, next_states):
        super().__init__(current_state, reward, next_states)
        self.next_states_dict = dict(next_states)

    def get_next_state(self, action):
        return self.next_states_dict[action]

    def set_node_for_reachabily(self):
        reward = 1 if self.is_final_node else 0
        return PlayerNode(self.player, self.current_state, reward, self.next_states)
    
    def get_best_strategies(self):
        max_probability = 0
        best_strategies = []
        # next_states_dict is a dict with the action as key and the state????? as value 
        # I might need to add the state list to get the next state properly. state_list[next_state_value]
        for action, next_state_value in self.next_states_dict: #.items()?
            if next_state_value.reach_probability > max_probability:
                max_probability = next_state_value.reach_probability
                best_strategies = [action]
            if next_state_value.reach_probability == max_probability:
                best_strategies.append(action)
        return best_strategies

    def prune_state(self, best_strategies):
        next_states_dict = {action: next_state for action, next_state in self.next_states_dict.items() if action in best_strategies}
        self.next_states_dict = next_states_dict
        self.next_states = list(next_states_dict.items())


class Solver:
    def __init__(self):
        pass

    def solve_reachability(self, state_list, transition_matrix, final_states):
        """This function returns a list of strategies for reachability"""
        reachable_states = self._get_reachable_states(transition_matrix, final_states)
        not_reachable_states = [state for state in state_list if state not in reachable_states]

        for state in not_reachable_states:
            state.reach_probability = 0

        for state in final_states:
            state.reach_probability = 1

        # Esto es bastante recursivo, hay que ver como hacerlo. Creo que acá hay que usar algoritmo de Bellman
        for state in reachable_states:
            if state.player == PLAYER_1:
                state.reach_probability = 0  #max de los reach_probabilities de los next states
            if state.player == PLAYER_2:
                state.reach_probability = 0  #min de los reach_probabilities de los next states
            if state.player == PROBABILISTIC:
                state.reach_probability = 0  #sum de los reach_probabilities de los next states por la probabilidad


        reachability_strategies = self._get_reachability_strategies(state_list)
        # Ahora para cada estado hay que ver cual es la mejor estrategia, 
        # puede ser que haya varias, que es el caso interesante, entonces devolvemos 
        # una lista de estrategias
        return reachability_strategies


    def solve_total_rewards(self, state_list, transition_matrix, reachability_strategies):
        """This function returns a list of strategies for total rewards.
            It receives a list of strategies that maximize reachability
            and it has to return a list of strategies that maximize total rewards for those strategies"""
        
        for idx, state in enumerate(state_list):
            if state.player == PLAYER_1:
                state.prune_state(reachability_strategies[idx])
        
        # Ahora que tenemos las estrategias recortadas, hay que hacerr algo similar a lo de solve reachability
        # donde calculamos los expected rewards para cada estado, y luego devolvemos la mejor estrategia

    def _get_reachable_states(self, transition_matrix, final_states):
        """This function returns a list of reachable states"""
        reverse_dfs(transition_matrix, final_states)

    def _get_reachability_strategies(self, state_list):
        """This function returns a list of strategies that maximize reachability"""
        strategies = [None] * len(state_list)
        for state in state_list:
            if state.player == PLAYER_1:
                strategies[state.current_state] = state.get_best_strategies()
        
        # strategies will be a list of lists, and it will have None if the player is not PLAYER_1
        # in the case of PLAYER_1, it will have a list of the best actions for that state
        
        # TODO it might be smarter to just prune the strategies for player one here 
        # and return state_list modified
        # and I could also return the strategies.
        return strategies
