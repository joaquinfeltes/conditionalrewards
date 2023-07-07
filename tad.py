import numpy as np
import random
from reverse_dfs import reverse_dfs

PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"
PROBABILISTIC = "Probabilistic"
ACTION = 0
PROBABILITY = 0
NEXT_STATE_IDX = 1
FIRST_PLAYER = 0
SECOND_PLAYER = 1
PROBABILISTIC_PLAYER = 2

class StochasticGame:
    """A stochastic game, with two players,
    a reward list, a set of final states and a transition matrix. All rewards are positive."""

    def __init__(self, reward_list, transition_matrix, final_states):
        self.reward_list = reward_list
        # TODO [yes] LIST OF TUPLES 
        # transition matrix could be a list of tuples, with the first element being
        # the player that controls the state, and the second element being the transition in that position
        self.transition_matrix = transition_matrix
        self.final_states = final_states
        self.num_states = len(self.transition_matrix[FIRST_PLAYER])

    def init_states(self):
        state_list = [None] * self.num_states
        if len(self.transition_matrix) != 3:
            raise ValueError("The transition matrix must have 3 elements, one for each player and one for the probabilistic nodes.")
        if len(self.transition_matrix[SECOND_PLAYER]) != self.num_states or \
            len(self.transition_matrix[PROBABILISTIC_PLAYER]) != self.num_states:
            raise ValueError("The transition matrix must have the same number of states for each player.")
        if len(self.reward_list) != self.num_states:
            raise ValueError("The reward list must have the same number of elements as states in the game.")

        for state_n, transitions in enumerate(self.transition_matrix[FIRST_PLAYER]):
            if transitions:
                state_list[state_n] = PlayerNode(
                    player=PLAYER_1, idx=state_n, next_states=transitions, reward=self.reward_list[state_n])

        for state_n, transitions in enumerate(self.transition_matrix[SECOND_PLAYER]):
            if transitions:
                state_list[state_n] = PlayerNode(
                    player=PLAYER_2, idx=state_n, next_states=transitions, reward=self.reward_list[state_n])

        for state_n, transitions in enumerate(self.transition_matrix[PROBABILISTIC_PLAYER]):
            if transitions:
                state_list[state_n] = ProbabilisticNode(
                    player=PROBABILISTIC, idx=state_n,
                    next_states=transitions, reward=self.reward_list[state_n], is_final_node=(state_n in self.final_states))

        if None in state_list:
            idx = state_list.index(None)
            raise ValueError(f"Transition for state {idx} is not defined")
        return state_list


    # TODO this two functions are literally just calling the solver, maybe we should just delete them
    def solve_reachability(self, state_list):
        reachability_strategies = Solver().solve_reachability(
            state_list=state_list,
              transition_matrix=self.transition_matrix, final_states=self.final_states)
        return reachability_strategies

    def solve_total_rewards(self, state_list, reachability_strategies):
        final_strategies = Solver().solve_total_rewards(state_list=state_list, transition_matrix=self.transition_matrix, reachability_strategies=reachability_strategies)
        return final_strategies

    def solve(self):
        state_list = self.init_states()
        reachability_strategies = self.solve_reachability(state_list)
        final_strategies = self.solve_total_rewards(state_list, reachability_strategies)
        return final_strategies


class Node:
    """The base node class
    idx: an int, is the number of the current state in the state list and the transition matrix
    next_states: a list of tuples, every tuple contains the next state and an action or a probability."""

    def __init__(self, player, idx, reward, next_states,
                 is_final_node=False):
        self.player = player
        self.idx = idx
        self.reward = reward
        self.next_states = next_states
        self.is_final_node = is_final_node
        self.reach_probability = 1 if is_final_node else 0
        self.reach_probability_next = 0
        self.expected_rewards = reward
        self.expected_rewards_next = 0

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return (
            self.player == other.player and
            self.idx == other.idx and
            self.reward == other.reward and
            self.next_states == other.next_states and
            self.is_final_node == other.is_final_node
        )


class ProbabilisticNode(Node):
    def __init__(self, player, idx, reward, next_states,
                 is_final_node):
        super().__init__(player, idx, reward, next_states, is_final_node)

    def value_iteration_reach(self, state_list):
        value = 0
        for next_state in self.next_states:
            _next_state = state_list[next_state[NEXT_STATE_IDX]]
            value += _next_state.reach_probability * next_state[PROBABILITY]
        return value

    def value_iteration_rewards(self, state_list):
        value = 0
        for next_state in self.next_states:
            _next_state = state_list[next_state[NEXT_STATE_IDX]]
            value += _next_state.expected_rewards * next_state[PROBABILITY]
        value += self.reward
        return value


# TODO: [YES] hacer una clase para cada jugador
class PlayerNode(Node):

    def __init__(self, player, idx, reward, next_states,
                 is_final_node=False):
        super().__init__(player, idx, reward, next_states, is_final_node)

    def value_iteration_reach_max(self, state_list):
        max_reach_prob = 0
        for _, next_state_idx in self.next_states:
            next_state_reach_prob = state_list[next_state_idx].reach_probability
            if next_state_reach_prob > max_reach_prob:
                max_reach_prob = next_state_reach_prob
        return max_reach_prob

    def value_iteration_reach_min(self, state_list):
        min_reach_prob = 1
        for next_state in self.next_states:
            next_state_reach_prob = state_list[next_state[NEXT_STATE_IDX]].reach_probability
            if next_state_reach_prob < min_reach_prob:
                min_reach_prob = next_state_reach_prob
        return min_reach_prob

    def get_best_strategies_reachability(self, state_list):
        max_probability = 0
        best_strategies = []
        for action, next_state_idx in self.next_states:
            next_state_reach_probability = state_list[next_state_idx].reach_probability 
            if next_state_reach_probability > max_probability:
                max_probability = next_state_reach_probability
                best_strategies = [action]
            elif next_state_reach_probability == max_probability:
                best_strategies.append(action)
        return best_strategies

    def prune_state(self, best_strategies):
        self.next_states = [(action, next_state) for action, next_state in self.next_states if action in best_strategies]

    def value_iteration_rewards_max(self, state_list):
        max_rewards = 0
        for next_state in self.next_states:
            next_state_exp_rewards = state_list[next_state[NEXT_STATE_IDX]].expected_rewards
            if next_state_exp_rewards > max_rewards:
                max_rewards = next_state_exp_rewards
        max_rewards += self.reward
        return max_rewards

    def value_iteration_rewards_min(self, state_list):
        # init min value with the value of the first state
        min_rewards = state_list[self.next_states[0][NEXT_STATE_IDX]].expected_rewards
        for next_state in self.next_states:
            next_state_exp_rewards = state_list[next_state[NEXT_STATE_IDX]].expected_rewards
            if next_state_exp_rewards < min_rewards:
                min_rewards = next_state_exp_rewards
        min_rewards += self.reward
        return min_rewards

    def get_best_strategies_total_rewards(self, state_list):
        max_rewards = 0
        best_strategies = []
        for action, next_state_idx in self.next_states:
            _next_state = state_list[next_state_idx]
            # TODO: [PEDRO] Recompensa condicionada
            # no estoy seguro si es acá o en cada iteracion del value iteration
            next_state_expected_rewards = _next_state.expected_rewards * _next_state.reach_probability
            if next_state_expected_rewards > max_rewards:
                max_rewards = next_state_expected_rewards
                best_strategies = [action]
            elif next_state_expected_rewards == max_rewards:
                best_strategies.append(action)
        return best_strategies


class Solver:
    def __init__(self, threshold=0.01):
        self.threshold = threshold
        #TODO add state list as an attribute

    def solve_reachability(self, state_list, transition_matrix, final_states):
        """This function calculates the probability to reach the final states for each state
            and returns a list of strategies for reachability for each state of player 1"""
        reachable_states = reverse_dfs(transition_matrix, final_states)
        self.value_iteration_reachability(reachable_states, state_list)
        reachability_strategies = self._get_reachability_strategies(state_list)
        return reachability_strategies

    def value_iteration_reachability(self, reachable_states, state_list):
        diff = 1
        while diff > self.threshold:
            for state_idx in reachable_states:
                state = state_list[state_idx]
                if state.player == PLAYER_1:
                    state.reach_probability_next = state.value_iteration_reach_max(state_list)
                elif state.player == PLAYER_2:
                    state.reach_probability_next = state.value_iteration_reach_min(state_list)
                elif state.player == PROBABILISTIC:
                    state.reach_probability_next = state.value_iteration_reach(state_list)
            
            diff = max([abs(state_list[state_idx].reach_probability_next - state_list[state_idx].reach_probability) for state_idx in reachable_states])
            for state_idx in reachable_states:
                state = state_list[state_idx]
                state.reach_probability = state.reach_probability_next

    def _get_reachability_strategies(self, state_list):
        """This function returns a list of strategies that maximize reachability for each state of player 1"""
        # strategies will be a list of lists, and it will have None if the player is not PLAYER_1
        # in the case of PLAYER_1, it will have a list of the best actions for that state
        strategies = [None] * len(state_list)
        for state in state_list:
            if state.player == PLAYER_1:
                strategies[state.idx] = state.get_best_strategies_reachability(state_list)
        return strategies


    def solve_total_rewards(self, state_list, transition_matrix, reachability_strategies):
        """This function returns a list of strategies for total rewards.
            It receives a list of strategies that maximize reachability
            and it has to return a list of strategies that maximize total rewards for those strategies"""
        
        # TODO [YES] NEW PRUNE function to better modularity
        # call it from stochastic games
        for idx, state in enumerate(state_list):
            if state.player == PLAYER_1:
                state.prune_state(reachability_strategies[idx])
                # TODO [mmm]: BORRAR NODOS
                # si cortamos un camino que llegaba a un nodo que no tiene otra forma de ser accedido, ese nodo ya no es alcanzable
                # pero no hace falta hacer nada al respecto, si no nos preocupa la eficiencia

        self.value_iteration_total_rewards(state_list)
        total_rewards_strategies = self._get_total_rewards_strategies(state_list)
        return total_rewards_strategies

    def value_iteration_total_rewards(self, state_list):
        diff = 1
        while diff > self.threshold:
            for state in state_list:
                if state.player == PLAYER_1:
                    state.expected_rewards_next = state.value_iteration_rewards_max(state_list)
                elif state.player == PLAYER_2:
                    state.expected_rewards_next = state.value_iteration_rewards_min(state_list)
                elif state.player == PROBABILISTIC:
                    state.expected_rewards_next = state.value_iteration_rewards(state_list)
            
            diff = max([abs(state.expected_rewards_next - state.expected_rewards) for state in state_list])
            for state in state_list:
                state.expected_rewards = state.expected_rewards_next

    def _get_total_rewards_strategies(self, state_list):
        """This function returns a list of strategies that maximize total rewards""" 
        strategies = [None] * len(state_list)
        for state in state_list:
            if state.player == PLAYER_1:
                strategies[state.idx] = state.get_best_strategies_total_rewards(state_list)
        return strategies