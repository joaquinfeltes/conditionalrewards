from reverse_dfs import reverse_dfs
import logging

PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"
PROBABILISTIC = "Probabilistic"
ACTION = 0
PROBABILITY = 0
NEXT_STATE_IDX = 1


class StochasticGame:
    """A stochastic game, with two players,
    a reward list, a set of final states and a transition matrix. All rewards are positive."""

    def __init__(self, rewards, players, transition_list, final_states):
        self.rewards = rewards
        self.players = players
        self.transition_list = transition_list
        self.final_states = final_states
        self.num_states = len(self.players)

    def check_game(self):
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

    def init_states(self):

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

    def only_one_strategy(self, strategies):
        for strategy in strategies:
            if strategy and len(strategy) > 1:
                return False
        return True

    def solve(self):
        logging.info("Initializing stochastic game ...")
        self.check_game()
        state_list = self.init_states()
        solver = Solver(threshold=10**(-6), state_list=state_list)

        logging.info("Solving reachability ...")
        reachability_strategies = solver.solve_reachability(
            self.transition_list, self.final_states)
        logging.debug(f"Reachability strategies: {reachability_strategies}")

        # if self.only_one_strategy(reachability_strategies):
        #     logging.info("Only one strategy left per node, no need to calculate total rewards.")
        #     logging.info("Done!")
        #     return reachability_strategies, reachability_strategies

        # This will leave us with a new state list,
        # where the states that can not reach the final states are removed
        # and the probability is distributed among the remaining states
        logging.info("Only keeping states with biggest probability to reach the objective ...")
        solver.prune_stochastich_game(reachability_strategies)

        logging.info("Solving total rewards ...")
        final_strategies = solver.solve_total_rewards()

        logging.info("Done!")
        return final_strategies, reachability_strategies


# TODO [5] remove this
def debug_states(state_list):
    for state in state_list:
        print(f"State: {state.idx}")
        print(f"Player: {state.player}")
        print(f"Reward: {state.reward}")
        print(f"Next states: {state.next_states}")
        print(f"Is final node: {state.is_final_node}")
        print(f"Reach probability: {state.reach_probability}")
        print(f"Expected rewards: {state.expected_rewards}")
        print("-"*80)


class Node:
    """The base node class
    idx: an int, is the number of the current state in the state list and the transition matrix
    next_states: a list of tuples,
    every tuple contains the next state and an action or a probability."""

    def __init__(self, player, idx, reward, next_states, num_states, is_final_node):
        self.player = player
        self.idx = idx
        self.reward = reward
        self.next_states = next_states
        self.is_final_node = is_final_node
        self.reach_probability = 1 if is_final_node else 0
        self.reach_probability_next = 0
        self.expected_rewards = reward
        self.expected_rewards_next = 0
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
        value = 0
        for next_state in self.next_states:
            _next_state = state_list[next_state[NEXT_STATE_IDX]]
            value += _next_state.reach_probability * next_state[PROBABILITY]
        return value

    def value_iteration_rewards(self, state_list):
        if not self.next_states:
            return 0
        value = 0
        for next_state in self.next_states:
            _next_state = state_list[next_state[NEXT_STATE_IDX]]
            value += _next_state.expected_rewards * next_state[PROBABILITY]
        value += self.reward
        return value

    # TODO [2]: test this
    def prune_paths(self, state_list):
        for _next_state in self.next_states:
            next_state = state_list[_next_state[NEXT_STATE_IDX]]
            if next_state.reach_probability == 0:
                self.remove_path(_next_state)

    def remove_path(self, state_to_remove):
        self.next_states.remove(state_to_remove)
        new_next_states = []
        # redistribute probability
        for _next_state in self.next_states:
            new_state_probability = _next_state[PROBABILITY] / (1 - state_to_remove[PROBABILITY])
            new_next_states.append((new_state_probability, _next_state[NEXT_STATE_IDX]))
        self.next_states = new_next_states


class PlayerOne(Node):

    def __init__(self, player, idx, reward, next_states, num_states, is_final_node=False):
        super().__init__(player, idx, reward, next_states, num_states, is_final_node)

    def value_iteration_reach(self, state_list):
        max_reach_prob = 0
        for _, next_state_idx in self.next_states:
            next_state_reach_prob = state_list[next_state_idx].reach_probability
            if next_state_reach_prob > max_reach_prob:
                max_reach_prob = next_state_reach_prob
        return max_reach_prob

    def value_iteration_rewards(self, state_list):
        if not self.next_states:
            return 0
        max_rewards = 0
        for next_state in self.next_states:
            next_state_exp_rewards = state_list[next_state[NEXT_STATE_IDX]].expected_rewards
            if next_state_exp_rewards > max_rewards:
                max_rewards = next_state_exp_rewards
        max_rewards += self.reward
        return max_rewards

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

    def prune_paths_reachability(self, best_strategies):
        self.next_states = [
            (action, next_state) for action, next_state in self.next_states
            if action in best_strategies]

    # TODO [2] test this
    def prune_paths(self, state_list):
        for _next_state in self.next_states:
            next_state = state_list[_next_state[NEXT_STATE_IDX]]
            if next_state.reach_probability == 0:
                self.remove_path(_next_state)

    def remove_path(self, state_to_remove):
        self.next_states.remove(state_to_remove)

    def get_best_strategies_total_rewards(self, state_list):
        max_rewards = 0
        best_strategies = []
        for action, next_state_idx in self.next_states:
            _next_state = state_list[next_state_idx]
            if _next_state.expected_rewards > max_rewards:
                max_rewards = _next_state.expected_rewards
                best_strategies = [action]
            elif _next_state.expected_rewards == max_rewards:
                best_strategies.append(action)
        return best_strategies


class PlayerTwo(Node):

    def __init__(self, player, idx, reward, next_states, num_states, is_final_node=False):
        super().__init__(player, idx, reward, next_states, num_states, is_final_node)

    def value_iteration_reach(self, state_list):
        min_reach_prob = 1
        for next_state in self.next_states:
            next_state_reach_prob = state_list[next_state[NEXT_STATE_IDX]].reach_probability
            if next_state_reach_prob < min_reach_prob:
                min_reach_prob = next_state_reach_prob
        return min_reach_prob

    def value_iteration_rewards(self, state_list):
        if not self.next_states:
            return 0
        # init min value with the value of the first state
        min_rewards = state_list[self.next_states[0][NEXT_STATE_IDX]].expected_rewards
        for next_state in self.next_states:
            next_state_exp_rewards = state_list[next_state[NEXT_STATE_IDX]].expected_rewards
            if next_state_exp_rewards < min_rewards:
                min_rewards = next_state_exp_rewards
        min_rewards += self.reward
        return min_rewards


class Solver:
    def __init__(self, state_list, threshold=10**(-6)):
        self.state_list = state_list
        self.threshold = threshold

    def solve_reachability(self, transition_list, final_states):
        """This function calculates the probability to reach the final states for each state
            and returns a list of strategies for reachability for each state of player 1"""

        if not final_states:
            raise ValueError("There must be at least one final state to solve reachability.")

        reachable_states = reverse_dfs(transition_list, final_states)
        self.value_iteration_reachability(reachable_states)
        reachability_strategies = self._get_reachability_strategies()
        return reachability_strategies

    def value_iteration_reachability(self, reachable_states):
        diff = 1
        logging.debug("Value iteration for reachability:")
        logging.debug("-"*80)
        i = 0
        while diff > self.threshold:
            logging.debug(f"iteration {i}")
            i += 1
            for state_idx in reachable_states:
                state = self.state_list[state_idx]
                state.reach_probability_next = state.value_iteration_reach(self.state_list)
            diff = max(
                [abs(self.state_list[state_idx].reach_probability_next -
                 self.state_list[state_idx].reach_probability) for state_idx in reachable_states])
            for state_idx in reachable_states:
                state = self.state_list[state_idx]
                logging.debug(f"{state.idx} {state.reach_probability}")
                state.reach_probability = state.reach_probability_next
            logging.debug("-"*80)
        logging.debug(f"iteration {i}")
        for state in self.state_list:
            logging.debug(f"{state.idx} {state.reach_probability}")
        logging.debug("-"*80)
        if self.state_list[0].reach_probability == 0:
            raise ValueError("The game has no solution.")

    def _get_reachability_strategies(self):
        """This function returns a list of strategies that maximize
        reachability for each state of player 1"""
        # strategies will be a list of lists, and it will have None if the player is not PLAYER_1
        # in the case of PLAYER_1, it will have a list of the best actions for that state
        strategies = [None] * len(self.state_list)
        for state in self.state_list:
            if state.player == PLAYER_1:
                strategies[state.idx] = state.get_best_strategies_reachability(self.state_list)
        return strategies

    def prune_stochastich_game(self, reachability_strategies):
        self.prune_paths(reachability_strategies)
        self.prune_states()

    def prune_paths(self, reachability_strategies):
        for idx, state in enumerate(self.state_list):
            if state.player == PLAYER_1:
                state.prune_paths_reachability(reachability_strategies[idx])
                state.prune_paths(self.state_list)
            if state.player == PROBABILISTIC:
                state.prune_paths(self.state_list)

    def prune_states(self):
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
        """This function returns a list of strategies for total rewards.
            It receives a list of strategies that maximize reachability
            and it has to return a list of strategies that maximize
            total rewards for those strategies"""
        self.value_iteration_total_rewards()
        total_rewards_strategies = self._get_total_rewards_strategies()
        return total_rewards_strategies

    def value_iteration_total_rewards(self):
        diff = 1
        logging.debug("Value iteration for total rewards:")
        logging.debug("-"*80)
        i = 0
        while diff > self.threshold:
            logging.debug(f"iteration {i}")
            i += 1
            for state in self.state_list:
                state.expected_rewards_next = state.value_iteration_rewards(self.state_list)

            diff = max([
                abs(state.expected_rewards_next - state.expected_rewards)
                for state in self.state_list])

            for state in self.state_list:
                logging.debug(f"{state.idx} {state.expected_rewards}")
                state.expected_rewards = state.expected_rewards_next
            logging.debug("-"*80)

        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            logging.debug(f"iteration {i}")
            for state in self.state_list:
                logging.debug(f"{state.idx} {state.expected_rewards}")
            logging.debug("-"*80)

    def _get_total_rewards_strategies(self):
        """This function returns a list of strategies that maximize total rewards"""
        strategies = [None] * len(self.state_list)
        for state in self.state_list:
            if state.player == PLAYER_1:
                strategies[state.idx] = state.get_best_strategies_total_rewards(self.state_list)
        return strategies
