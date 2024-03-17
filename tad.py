from reverse_dfs import reverse_dfs
import logging
import math

PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"
PROBABILISTIC = "Probabilistic"
ACTION = 0
PROBABILITY = 0
NEXT_STATE_IDX = 1

# 1 TODO: calcular las cosas que nos faltan en la tabla 1 (esto puede hacer fallar los tests tambien )
# 2 TODO: fallan los tests,pq agregué output nuevos, solo tengo que agregar lo nuevo

class StochasticGame:
    """
        A stochastic game with positive rewards.
        rewards: a list of positive integers, one for each state.
        players: a list of strings, one for each state. 
            The string can be "Player 1", "Player 2" or "Probabilistic".
        transition_list: a list of lists of tuples, one for each state.
            Each tuple contains an action or a probability and the next state.
        final_states: a list of integers, the indexes of the final states.
        prune_states: a boolean, if True, the states with no reachability will be pruned.
            If we prune the states, we are calculating the expected rewards conditioned to reachability.
    """

    def __init__(self, rewards, players, transition_list, final_states, prune_states=True):
        self.rewards = rewards
        self.players = players
        self.transition_list = transition_list
        self.final_states = final_states
        self.num_states = len(self.players)
        self.prune_states = prune_states

    def check_game(self):
        """
            Check that the game is well defined.
        """
        if len(self.transition_list) != self.num_states:
            raise ValueError(
                "The transition list must have the same number of elements as states in the game.")

        if len(self.rewards) != self.num_states:
            raise ValueError(
                "The reward list must have the same number of elements as states in the game.")

        if min(self.rewards) < 0:
            raise ValueError("Rewards must be positive.")

        if max(self.final_states) >= self.num_states or min(self.final_states) < 0:
            raise ValueError("Final states must be in the range of the number of states.")

        for player in self.players:
            if player not in [PLAYER_1, PLAYER_2, PROBABILISTIC]:
                raise ValueError(f"Player must be {PLAYER_1}, {PLAYER_2} or {PROBABILISTIC}.")

    def count_transitions(self):
        """
            Count the number of transitions in the game.
        """
        transitions = 0
        for state_transitions in self.transition_list:
            transitions += len(state_transitions)
        return transitions

    def init_states(self):
        """
            This function initializes the states of the game.
            Every player has a different state object.

            Output:
                state_list: a list of state objects.
        """
        state_list = []
        for idx, (player, transitions, reward) in enumerate(
                zip(self.players, self.transition_list, self.rewards)):
            if transitions:
                if player == PLAYER_1:
                    state_list.append(PlayerOne(
                        player=player, idx=idx, next_states=transitions,
                        reward=reward, num_states=self.num_states,
                        is_final_node=(idx in self.final_states)))

                elif player == PLAYER_2:
                    state_list.append(PlayerTwo(
                        player=player, idx=idx, next_states=transitions,
                        reward=reward, num_states=self.num_states,
                        is_final_node=(idx in self.final_states)))

                elif player == PROBABILISTIC:
                    state_list.append(ProbabilisticNode(
                        player=player, idx=idx, next_states=transitions,
                        reward=reward, num_states=self.num_states,
                        is_final_node=(idx in self.final_states)))
        if not len(state_list) == self.num_states:
            raise ValueError("Missing transitions")
        return state_list

    def solve(self):
        """
            Main function to solve the stochastic game.
            First it initializes the states of the game.
            Then it runs the reachability algorithm.
            If prune_states is True, it prunes the states with no reachability.
            Last, it runs the total rewards algorithm.

            Output:
                final_strategies: a list of strategies for total rewards.
                reachability_strategies: a list of strategies for reachability.
                rewards: a list of expected rewards for each state.
                probabilities: a list of reachability probabilities for each state.
        """
        logging.info("Initializing stochastic game ...")
        self.check_game()
        state_list = self.init_states()
        solver = Solver(threshold=10**(-6), state_list=state_list)

        logging.info("Solving reachability ...")
        reachability_strategies, n_iterations_reach = solver.solve_reachability(
            self.transition_list, self.final_states, self.prune_states)
        probabilities = [state.reach_probability for state in state_list]
        logging.debug(f"Reachability strategies: {reachability_strategies}")

        if self.prune_states:
            logging.info("Prunning states with no reachability ...")
            solver.prune_stochastich_game(reachability_strategies)
        else:
            logging.info("Not prunning states.")

        logging.info("Solving total rewards ...")
        final_strategies, n_iterations_rew = solver.solve_total_rewards()
        rewards = [state.expected_rewards for state in state_list]
        expected_reach_min_rewards = [0] * self.num_states # TODO HACER ESTE
        expected_rewards_min_reach = [state.expected_rewards_min_reach for state in state_list]
        
        logging.info("Done!")
        return final_strategies, reachability_strategies, rewards, probabilities, n_iterations_reach, n_iterations_rew, expected_reach_min_rewards, expected_rewards_min_reach


class Node:
    """
        The base node class
        player: a string, the player of the node.
        idx: an int, the number of the current state in the state list and the transition matrix.
        reward: an int, the reward of the state.
        next_states: a list of tuples, every tuple contains the next state and an action or a probability.
        num_states: an int, the number of states in the game.
        is_final_node: a boolean, True if the state is a final state.
    """

    def __init__(self, player, idx, reward, next_states, num_states, is_final_node):
        self.player = player
        self.idx = idx
        self.reward = reward
        self.next_states = next_states
        self.is_final_node = is_final_node
        self.reach_probability = 1 if is_final_node else 0
        # reach_probability_next can be a variable of the value iteration function, its not neccessary in the class
        self.expected_rewards = reward
        self.expected_rewards_min_reach = reward
        self.expected_reach_min_rewards = 0
        self.num_states = num_states
        self.check_next_states()

    def __eq__(self, other):
        return (
            self.player == other.player and
            self.idx == other.idx and
            self.reward == other.reward and
            self.next_states == other.next_states and
            self.is_final_node == other.is_final_node
        )

    def check_next_states(self):
        """
            Check if the next states are well defined.
        """
        if not isinstance(self.next_states, list):
            raise ValueError("Next states must be a list.")

        for next_state in self.next_states:
            if not isinstance(next_state, tuple):
                raise ValueError("Next states must be a list of tuples.")

            if len(next_state) != 2:
                raise ValueError("Next states must be a list of tuples of length 2.")

            if self.player == PLAYER_1 or self.player == PLAYER_2:
                if not isinstance(next_state[ACTION], str):
                    raise ValueError("The action must be a str.")

            elif self.player == PROBABILISTIC:
                if not isinstance(next_state[PROBABILITY], (int, float)):
                    raise ValueError("The probability must be a number.")

            if not isinstance(next_state[NEXT_STATE_IDX], int):
                raise ValueError("The next state must be an int.")

            if next_state[NEXT_STATE_IDX] < 0 or next_state[NEXT_STATE_IDX] >= self.num_states:
                raise ValueError("The next state must be in the range of the number of states.")


class ProbabilisticNode(Node):
    def __init__(self, player, idx, reward, next_states, num_states, is_final_node):
        super().__init__(player, idx, reward, next_states, num_states, is_final_node)

    def value_iteration_reach(self, state_list):
        """
            A step of the value iteration algorithm for reachability.
            It returns the reach probability of the next states 
            weighted by the probability to reach that state.
        """
        value = 0
        for next_state in self.next_states:
            _next_state = state_list[next_state[NEXT_STATE_IDX]]
            value += _next_state.reach_probability * next_state[PROBABILITY]
        return value
    

    # TODO: CORRER ESTA ITERACION DESPUES DE TENER LAS ESTRATEGIAS DE RECOMPENSA
    # TODO: CORRER ESTA ITERACION DESPUES DE TENER LAS ESTRATEGIAS DE RECOMPENSA
    # TODO: CORRER ESTA ITERACION DESPUES DE TENER LAS ESTRATEGIAS DE RECOMPENSA
    # TODO: CORRER ESTA ITERACION DESPUES DE TENER LAS ESTRATEGIAS DE RECOMPENSA
    # creo que debería iterar por todo de nuevo, para que se actualicen los valores,
    # o sea seria otro value iteration, pero para una MC porque la estrategia está fija, solo quiero calcular el valor
    # def _iteration_reach_min_rewards(self, state_list):
    #     """ QUE LE ENTRE LA ESTRATEGIA, CUANDO YA ESTA TERMINADO EL ALGORITMO
    #     """
    #     value = 0
    #     for next_state in self.next_states:
    #         _next_state = state_list[next_state[NEXT_STATE_IDX]]
    #         value += _next_state.expected_reach_min_rewards * next_state[PROBABILITY]
    #     return value

    def value_iteration_rewards(self, state_list):
        """
            A step of the value iteration algorithm for total rewards.
            It returns the rewards of the next states 
            weighted by the probability to reach that state
            plus the reward of the current state.
        """
        if not self.next_states:
            return 0, 0
        value = 0
        expected_rewards_min_reach = 0
        for next_state in self.next_states:
            _next_state = state_list[next_state[NEXT_STATE_IDX]]
            value += _next_state.expected_rewards * next_state[PROBABILITY]
            expected_rewards_min_reach += _next_state.expected_rewards_min_reach * next_state[PROBABILITY]
        value += self.reward
        expected_rewards_min_reach += self.reward
        return value, expected_rewards_min_reach

    def prune_paths(self, state_list):
        """
            Removes the next states that have
            zero probability of reaching the final states.
        """
        for _next_state in self.next_states:
            next_state = state_list[_next_state[NEXT_STATE_IDX]]
            if next_state.reach_probability == 0:
                self.remove_path(_next_state)

    def remove_path(self, state_to_remove):
        """
            It removes a state from the next states and redistributes the probability.
        """
        self.next_states.remove(state_to_remove)
        new_next_states = []
        for _next_state in self.next_states:
            new_state_probability = _next_state[PROBABILITY] / (1 - state_to_remove[PROBABILITY])
            new_next_states.append((new_state_probability, _next_state[NEXT_STATE_IDX]))
        self.next_states = new_next_states


class PlayerOne(Node):

    def __init__(self, player, idx, reward, next_states, num_states, is_final_node=False):
        super().__init__(player, idx, reward, next_states, num_states, is_final_node)

    def value_iteration_reach(self, state_list):
        """
            A step of the value iteration algorithm for reachability.
            It returns the maximum reach probability of the next states.
        """
        max_reach_prob = 0
        for _, next_state_idx in self.next_states:
            next_state_reach_prob = state_list[next_state_idx].reach_probability
            if next_state_reach_prob > max_reach_prob:
                max_reach_prob = next_state_reach_prob
        return max_reach_prob


# creo que debería iterar por todo de nuevo, para que se actualicen los valores,
    # o sea seria otro value iteration, pero para una MC porque la estrategia está fija, solo quiero calcular el valor
    # def _iteration_reach_min_rewards(self, state_list, action):
    #     """ QUE LE ENTRE LA ESTRATEGIA, CUANDO YA ESTA TERMINADO EL ALGORITMO
    #     """
    #     next_state = [ns for ns in self.next_states if ns[ACTION] == action][0]
    #     next_state_reach_prob = state_list[next_state[NEXT_STATE_IDX]].expected_reach_min_rewards
    #     return next_state_reach_prob


    def value_iteration_rewards(self, state_list):
        """
            A step of the value iteration algorithm for total rewards.
            It returns the maximum rewards of the next states plus the reward of the current state.
            If there are no next states, it returns 0.
        """
        if not self.next_states:
            return 0, 0
        max_rewards = 0
        for next_state in self.next_states:
            next_state_exp_rewards = state_list[next_state[NEXT_STATE_IDX]].expected_rewards
            if next_state_exp_rewards >= max_rewards:
                max_rewards = next_state_exp_rewards
                max_next_state = next_state
        max_rewards += self.reward
        expected_rewards_min_reach = state_list[max_next_state[NEXT_STATE_IDX]].expected_rewards_min_reach + self.reward
        return max_rewards, expected_rewards_min_reach

    def get_best_strategies_reachability(self, state_list, floor):
        """
            Returns the strategies with the maximum reach probability.
        """
        max_probability = 0
        best_strategies = []
        for action, next_state_idx in self.next_states:
            next_state_reach_probability = round(
                state_list[next_state_idx].reach_probability, floor)
            if next_state_reach_probability > max_probability:
                max_probability = next_state_reach_probability
                best_strategies = [action]
            elif next_state_reach_probability == max_probability:
                best_strategies.append(action)
        return best_strategies

    def prune_paths_reachability(self, best_strategies):
        """
            Only keeps the next states that have the best probability of
            reaching the final states.
        """
        self.next_states = [
            (action, next_state) for action, next_state in self.next_states
            if action in best_strategies]

    def prune_paths(self, state_list):
        """
            Removes the next states that have zero probability of reaching
            the final states.
        """
        for _next_state in self.next_states:
            next_state = state_list[_next_state[NEXT_STATE_IDX]]
            if next_state.reach_probability == 0:
                self.remove_path(_next_state)

    def remove_path(self, state_to_remove):
        """ 
            It removes a state from the next states.
        """
        self.next_states.remove(state_to_remove)

    def get_best_strategies_total_rewards(self, state_list, floor):
        """
            Returns the strategies with the maximum expected rewards.
        """
        max_rewards = 0
        best_strategies = []
        for action, next_state_idx in self.next_states:
            next_state_expected_rewards = round(state_list[next_state_idx].expected_rewards, floor)
            if next_state_expected_rewards > max_rewards:
                max_rewards = next_state_expected_rewards
                best_strategies = [action]
            elif next_state_expected_rewards == max_rewards:
                best_strategies.append(action)
        return best_strategies


class PlayerTwo(Node):

    def __init__(self, player, idx, reward, next_states, num_states, is_final_node=False):
        super().__init__(player, idx, reward, next_states, num_states, is_final_node)

    def value_iteration_reach(self, state_list):
        """
            A step of the value iteration algorithm for reachability.
            It returns the minimum reach probability of the next states.
        """
        min_reach_prob = 1
        for next_state in self.next_states:
            next_state_reach_prob = state_list[next_state[NEXT_STATE_IDX]].reach_probability
            if next_state_reach_prob < min_reach_prob:
                min_reach_prob = next_state_reach_prob
        return min_reach_prob

# creo que debería iterar por todo de nuevo, para que se actualicen los valores,
    # o sea seria otro value iteration, pero para una MC porque la estrategia está fija, solo quiero calcular el valor
    # def _iteration_reach_min_rewards(self, state_list, strategies):
    #     """ QUE LE ENTRE LA ESTRATEGIA, CUANDO YA ESTA TERMINADO EL ALGORITMO
    #     """
    # # PUEDEN HABER VARIAS ESTRATEGIAS QUE MINIMIZAN LA RECOMPENSA
    #     next_state = [ns for ns in self.next_states if ns[ACTION] == action]
    #     next_state_reach_prob = state_list[next_state[NEXT_STATE_IDX]].expected_reach_min_rewards
    #     return next_state_reach_prob

    def _expected_rewards_min_reach(self, state_list, strategies):
        """
            Returns the expected rewards conditioned on the reachability objectives.
        """
        if not strategies:
            return 0
        first_n_state = [next_state for next_state in self.next_states if next_state[ACTION] in strategies][0]
        min_rewards = state_list[first_n_state[NEXT_STATE_IDX]].expected_rewards_min_reach
        for next_state in self.next_states:
            if next_state[ACTION] in strategies:
                next_state_exp_rewards = state_list[next_state[NEXT_STATE_IDX]].expected_rewards_min_reach
                if next_state_exp_rewards < min_rewards:
                    min_rewards = next_state_exp_rewards
        min_rewards += self.reward
        return min_rewards


    def value_iteration_rewards(self, state_list):
        """
            A step of the value iteration algorithm for total rewards.
            It returns the minimum rewards of the next states plus the reward of the current state.
            If there are no next states, it returns 0.
        """
        if not self.next_states:
            return 0, 0
        reachability_strategies = self.get_worst_strategies_reachability(state_list, 6)
        expected_rewards_min_reach = self._expected_rewards_min_reach(state_list, reachability_strategies)
        # init min value with the value of the first state
        min_rewards = state_list[self.next_states[0][NEXT_STATE_IDX]].expected_rewards
        for next_state in self.next_states:
            next_state_exp_rewards = state_list[next_state[NEXT_STATE_IDX]].expected_rewards
            if next_state_exp_rewards < min_rewards:
                min_rewards = next_state_exp_rewards
        min_rewards += self.reward
        return min_rewards, expected_rewards_min_reach
    
    def get_worst_strategies_reachability(self, state_list, floor):
        """
            Returns the strategies with the minimum reach probability.
        """
        min_reach_prob = 1
        worst_strategies = []
        for action, next_state_idx in self.next_states:
            next_state_reach_probability = round(
                state_list[next_state_idx].reach_probability, floor)
            if next_state_reach_probability < min_reach_prob:
                min_reach_prob = next_state_reach_probability
                worst_strategies = [action]
            elif next_state_reach_probability == min_reach_prob:
                worst_strategies.append(action)
        return worst_strategies
    
    def get_worst_strategies_total_rewards(self, state_list, floor):
        """
            Returns the strategies with the maximum expected rewards.
        """
        if len(self.next_states) == 0:
            return []
        min_rewards = round(state_list[self.next_states[0][NEXT_STATE_IDX]].expected_rewards, floor)
        worst_strategies = []
        for action, next_state_idx in self.next_states:
            next_state_expected_rewards = round(state_list[next_state_idx].expected_rewards, floor)
            if next_state_expected_rewards < min_rewards:
                min_rewards = next_state_expected_rewards
                worst_strategies = [action]
            elif next_state_expected_rewards == min_rewards:
                worst_strategies.append(action)
        return worst_strategies


class Solver:
    def __init__(self, state_list, threshold=10**(-6)):
        self.state_list = state_list
        self.threshold = threshold
        self.floor = abs(math.floor(math.log(threshold, 10)))

    def solve_reachability(self, transition_list, final_states, prune_states):
        """
            Calculates the probability to reach the final states for each state
            and returns a list of strategies for maximize reachability for each state of player 1
            and a list of strategies for minimize reachability for each state of player 2.
        """

        if not final_states:
            raise ValueError("There must be at least one final state to solve reachability.")

        states_reaching_final = reverse_dfs(transition_list, final_states)
        n_iterations_reach = self.value_iteration_reachability(states_reaching_final, prune_states)
        reachability_strategies = self._get_reachability_strategies()
        return reachability_strategies, n_iterations_reach

    def value_iteration_reachability(self, states_reaching_final, prune_states):
        """
            Calculates the probability to reach the final states for each state.
            It uses the value iteration algorithm to calculate the reachability probabilities.
            It stops when the difference between the reach probabilities of two consecutive
            iterations is less than the threshold.
            If the initial state has a reach probability of 0, it raises an error.
        """
        diff = 1
        logging.debug("Value iteration for reachability:")
        logging.debug("-"*80)
        i = 0
        while diff > self.threshold:
            logging.debug(f"iteration {i}")
            i += 1
            max_diff = 0
            for state_idx in states_reaching_final:
                state = self.state_list[state_idx]
                reach_probability_next = state.value_iteration_reach(self.state_list)
                current_diff = abs(reach_probability_next - state.reach_probability)
                if current_diff > max_diff:
                    max_diff = current_diff
                logging.debug(f"{state.idx} {state.reach_probability}")
                state.reach_probability = reach_probability_next
            diff = max_diff

            logging.debug("-"*80)
        logging.debug(f"iteration {i}")
        for state in self.state_list:
            logging.debug(f"{state.idx} {state.reach_probability}")
            state.expected_reach_min_rewards = state.reach_probability
        logging.debug("-"*80)

        if self.state_list[0].reach_probability == 0 and prune_states:
            raise ValueError("The game has no solution. The initial state has a reach probability of 0.")
        return i

    def _get_reachability_strategies(self):
        """
            Returns a list of strategies for every state.
            For player 1 nodes, a list of the best actions that maximize reachability for each state.
            For player 2 nodes, a list of the best actions that minimize reachability for each state.
            For prababilistic nodes, it returns None in that position.
        """
        strategies = [None] * len(self.state_list)
        for state in self.state_list:
            if state.player == PLAYER_1:
                strategies[state.idx] = state.get_best_strategies_reachability(
                    self.state_list, self.floor)
            elif state.player == PLAYER_2:
                strategies[state.idx] = state.get_worst_strategies_reachability(
                    self.state_list, self.floor)
        return strategies

    def prune_stochastich_game(self, reachability_strategies):
        self.prune_paths(reachability_strategies)
        self.prune_states()

    def prune_paths(self, reachability_strategies):
        """
            Removes the paths of the next states that have a probability of zero of reaching
            the final states for player 1 and probabilistic nodes.
            Aslo for player 1 it only keeps the paths that have the best probability of
            reaching the final states .
        """
        for idx, state in enumerate(self.state_list):
            if state.player == PLAYER_1:
                state.prune_paths_reachability(reachability_strategies[idx])
                state.prune_paths(self.state_list)
            if state.player == PROBABILISTIC:
                state.prune_paths(self.state_list)

    def prune_states(self):
        """
            Removes the states for player 2 and probabilistic that cannot be
            reached from another state.
            It keeps the states for player 1 that can't be reached because we
            don't know if player 2 is going to choose the strategy that
            minimizes reachability or not.
        """
        finished = False
        not_reachable_states = []

        while not finished:
            reachable_states = [0]
            not_reachable_states_new = []
            for state in self.state_list:
                for next_state in state.next_states:
                    reachable_states.append(next_state[NEXT_STATE_IDX])

            for idx, state in enumerate(self.state_list):
                if state.player != PLAYER_1 and idx not in reachable_states:
                    not_reachable_states_new.append(idx)
                    self.state_list[idx].next_states = []
                elif state.player == PLAYER_1 and not state.next_states \
                        and idx not in reachable_states:
                    not_reachable_states_new.append(idx)
            finished = set(not_reachable_states_new) == set(not_reachable_states)
            not_reachable_states = not_reachable_states_new

    def solve_total_rewards(self):
        """
            Returns a list of strategies for total rewards.
            It receives a list of strategies that maximize reachability
            and it has to return a list of strategies that maximize
            total rewards for those strategies.
        """
        n_iterations_rew = self.value_iteration_total_rewards()
        total_rewards_strategies = self._get_total_rewards_strategies()
        return total_rewards_strategies, n_iterations_rew

    def value_iteration_total_rewards(self):
        """ 
            Calculates the expected rewards for each state.
            It uses the value iteration algorithm to calculate the expected rewards.
            It stops when the difference between the expected rewards of two consecutive
            iterations is less than the threshold.
        """
        diff = 1
        logging.debug("Value iteration for total rewards:")
        logging.debug("-"*80)
        i = 0
        # import ipdb; ipdb.set_trace()
        while diff > self.threshold:
            logging.debug(f"iteration {i}")
            i += 1
            max_diff = 0
            for state in self.state_list:
                expected_rewards_next, expected_rewards_min_reach = state.value_iteration_rewards(self.state_list)
                current_diff_expected_rew = abs(expected_rewards_next - state.expected_rewards)
                current_diff_min_reach = abs(expected_rewards_min_reach - state.expected_rewards_min_reach)
                current_diff = max(current_diff_expected_rew, current_diff_min_reach)
                if current_diff > max_diff:
                        max_diff = current_diff    
                logging.debug(f"{state.idx} {state.expected_rewards}")
            # for state in self.state_list: #ACABO DE METER ESTO, QUE DEBERIA ACTUALIZAR EL 
                #VECTOR DESPUES DE TERMINAR UNA ITER, PERO VEMO
                state.expected_rewards = expected_rewards_next
                state.expected_rewards_min_reach = expected_rewards_min_reach
            logging.debug("-"*80)
            diff = max_diff

        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(f"iteration {i}")
            for state in self.state_list:
                logging.debug(f"{state.idx} {state.expected_rewards}")
            logging.debug("-"*80)
        return i

    def _get_total_rewards_strategies(self):
        """
            Returns a list of strategies that maximize total rewards.
        """
        strategies = [None] * len(self.state_list)
        for state in self.state_list:
            if state.player == PLAYER_1:
                strategies[state.idx] = state.get_best_strategies_total_rewards(
                    self.state_list, self.floor)
            elif state.player == PLAYER_2:
                strategies[state.idx] = state.get_worst_strategies_total_rewards(
                    self.state_list, self.floor)
        return strategies
