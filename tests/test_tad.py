import pytest
import math

from tad import (
    PLAYER_1,
    PLAYER_2,
    PROBABILISTIC,
    Solver
)

FLOOR_ = abs(math.floor(math.log(10**(-6), 10)))


def init_reachability(state_list, reach_probability_list):
    # Hardcode the reach probability to each state
    for state, reach_probability in zip(state_list, reach_probability_list):
        state.reach_probability = reach_probability


# ----------------------------------------StochasticGame----------------------------------------#

def test_sg_init_states(stochastic_game_game_5_5, state_list_game_5_5):
    state_list = stochastic_game_game_5_5.init_states()
    for state, expected_state in zip(state_list, state_list_game_5_5):
        assert state == expected_state


def test_sg_init_states_missing_transition(stochastic_game_first_state_without_transitions):
    with pytest.raises(ValueError) as e:
        stochastic_game_first_state_without_transitions.init_states()
    assert str(e.value) == "Missing transitions"


def test_sg_check_game_incomplete_rewards(stochastic_game_incomplete_rewards):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_rewards.check_game()
    assert str(e.value) == \
        "The reward list must have the same number of elements as states in the game."


def test_sg_check_game_incomplete_players(stochastic_game_incomplete_players):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_players.check_game()
    assert str(e.value) == \
        "The transition list must have the same number of elements as states in the game."


def test_sg_check_game_negative_rewards(stochastic_game_negative_rewards):
    with pytest.raises(ValueError) as e:
        stochastic_game_negative_rewards.check_game()
    assert str(e.value) == "Rewards must be positive."


def test_sg_check_game_final_out_of_range_min(stochastic_game_final_out_of_range_min):
    with pytest.raises(ValueError) as e:
        stochastic_game_final_out_of_range_min.check_game()
    assert str(e.value) == "Final states must be in the range of the number of states."


def test_sg_check_game_final_out_of_range_max(stochastic_game_final_out_of_range_max):
    with pytest.raises(ValueError) as e:
        stochastic_game_final_out_of_range_max.check_game()
    assert str(e.value) == "Final states must be in the range of the number of states."


def test_sg_check_game_unknown_player(stochastic_game_unknown_player):
    with pytest.raises(ValueError) as e:
        stochastic_game_unknown_player.check_game()
    assert str(e.value) == f"Player must be {PLAYER_1}, {PLAYER_2} or {PROBABILISTIC}."


def test_sg_check_game_incomplete_transition_list(stochastic_game_incomplete_transition_list):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_transition_list.check_game()
    assert str(e.value) == \
        "The transition list must have the same number of elements as states in the game."


def test_sg_solve(stochastic_game_game_5_5):
    final_strategies, reachability_strategies, rewards, probabilities  = stochastic_game_game_5_5.solve()
    # prune states is True, so there is no rewards for the states that are pruned
    # and the reward is the conditional reward
    # also as some player 2 states are pruned, they don't have final strategies
    expected_final_strategies = [["beta"], [], ["x"], None, None, None, None, None]
    expected_reachability_strategies = [["beta"], ["x"], ["x"], None, None, None, None, None]
    assert final_strategies == expected_final_strategies
    assert reachability_strategies == expected_reachability_strategies
    state_2_rewards = stochastic_game_game_5_5.rewards[2]
    assert rewards == [state_2_rewards, 0, state_2_rewards, 0, 0, 0, 0, 0]
    assert probabilities == [0.75, 0.5, 0.75, 0.5, 0.75, 0, 1, 0] 


def test_sg_solve_same_reach(stochastic_game_game_5_5_same_reach):
    final_strategies, reachability_strategies, rewards, probabilities = stochastic_game_game_5_5_same_reach.solve()
    expected_final_strategies = [["alfa"], ["x"], ["x"], None, None, None, None, None]
    expected_reachability_strategies = [["alfa", "beta"], ["x"], ["x"], None, None, None, None, None]
    assert final_strategies == expected_final_strategies
    assert reachability_strategies == expected_reachability_strategies
    state_1_rewards = stochastic_game_game_5_5_same_reach.rewards[1]
    state_2_rewards = stochastic_game_game_5_5_same_reach.rewards[2]

    assert rewards == [state_1_rewards, state_1_rewards, state_2_rewards, 0, 0, 0, 0, 0]
    assert probabilities == [0.5, 0.5, 0.5, 0.5, 0.5, 0, 1, 0] 


def test_sg_check_next_states_wrong_type_list(stochastic_game_next_states_wrong_type_list):
    with pytest.raises(ValueError) as e:
        stochastic_game_next_states_wrong_type_list.init_states()
    assert str(e.value) == "Next states must be a list."


def test_sg_check_next_states_wrong_type_tuple(stochastic_game_next_states_wrong_type_tuple):
    with pytest.raises(ValueError) as e:
        stochastic_game_next_states_wrong_type_tuple.init_states()
    assert str(e.value) == "Next states must be a list of tuples."


def test_sg_check_next_states_wrong_length(stochastic_game_next_states_bigger_tuple):
    with pytest.raises(ValueError) as e:
        stochastic_game_next_states_bigger_tuple.init_states()
    assert str(e.value) == "Next states must be a list of tuples of length 2."


def test_sg_check_next_states_wrong_action_type(stochastic_game_next_states_wrong_action):
    with pytest.raises(ValueError) as e:
        stochastic_game_next_states_wrong_action.init_states()
    assert str(e.value) == "The action must be a str."


def test_sg_check_next_states_wrong_prob(stochastic_game_next_states_wrong_prob):
    with pytest.raises(ValueError) as e:
        stochastic_game_next_states_wrong_prob.init_states()
    assert str(e.value) == "The probability must be a number."


def test_sg_check_next_states_wrong_state_type(stochastic_game_next_states_wrong_state_type):
    with pytest.raises(ValueError) as e:
        stochastic_game_next_states_wrong_state_type.init_states()
    assert str(e.value) == "The next state must be an int."


def test_sg_check_next_states_wrong_state_idx(stochastic_game_next_states_wrong_state_idx):
    with pytest.raises(ValueError) as e:
        stochastic_game_next_states_wrong_state_idx.init_states()
    assert str(e.value) == "The next state must be in the range of the number of states."


# ----------------------------------------ProbabilisticNode----------------------------------------#

def test_probabilistic_value_iteration_reach(node_0, state_list_simple):
    assert node_0.value_iteration_reach(state_list_simple) == 0.5


def test_probabilistic_value_iteration_rewards(node_0, state_list_simple):
    assert node_0.value_iteration_rewards(state_list_simple) == 3.5


def test_probabilistic_prune_paths(node_0, state_list_simple):
    assert node_0.next_states == [(0.5, 1), (0.5, 2)]
    node_0.prune_paths(state_list_simple)
    assert node_0.next_states == [(1, 1)]


def test_probabilistic_remove_path(node_0_prob, state_list_all_prob):
    first_neighboor = node_0_prob.next_states[0]
    second_neighboor = node_0_prob.next_states[1]
    third_neighboor = node_0_prob.next_states[2]
    node_0_prob.remove_path(first_neighboor)
    new_total = second_neighboor[0] + third_neighboor[0]
    expected_second_neighboor = (second_neighboor[0]/new_total, second_neighboor[1])
    expected_third_neighboor = (third_neighboor[0]/new_total, third_neighboor[1])
    assert node_0_prob.next_states == [expected_second_neighboor, expected_third_neighboor]

# ----------------------------------------PlayerOne----------------------------------------#


def test_player_one_value_iteration_reach(player_one_node_0, state_list_w_player_one_at_start):
    reachability = player_one_node_0.value_iteration_reach(state_list_w_player_one_at_start)
    expected_reachability = 1
    assert reachability == expected_reachability


def test_player_one_value_iteration_rewards(
        player_one_node_0, state_list_w_player_one_at_start):
    total_rewards = player_one_node_0.value_iteration_rewards(state_list_w_player_one_at_start)
    expected_total_rewards = 4
    assert total_rewards == expected_total_rewards


def test_player_one_get_best_strategies_reachability(
        player_one_node_0, state_list_w_player_one_at_start):
    expected_best_strategies = ["a"]
    assert player_one_node_0.get_best_strategies_reachability(state_list_w_player_one_at_start, FLOOR_) == \
        expected_best_strategies


def test_player_one_get_best_strategies_reachability_two_strategies(
        player_one_node_0, state_list_two_final_states):
    expected_best_strategies = ["a", "b"]
    assert player_one_node_0.get_best_strategies_reachability(state_list_two_final_states, FLOOR_) == \
        expected_best_strategies


def test_player_one_prune_paths_reachability(player_one_node_0):
    best_strategies = ["a"]
    assert player_one_node_0.next_states == [("a", 1), ("b", 2)]
    player_one_node_0.prune_paths_reachability(best_strategies)
    assert player_one_node_0.next_states == [("a", 1)]


def test_player_one_prune_paths(player_one_node_0, state_list_w_player_one_at_start):
    assert player_one_node_0.next_states == [("a", 1), ("b", 2)]
    player_one_node_0.prune_paths(state_list_w_player_one_at_start)
    assert player_one_node_0.next_states == [("a", 1)]


def test_player_one_get_best_strategies_total_rewards(
        player_one_node_0, state_list_w_player_one_at_start):
    # The best strategy is "b" because it has more rewards
    expected_best_strategies = ["b"]
    assert player_one_node_0.get_best_strategies_total_rewards(
        state_list_w_player_one_at_start, FLOOR_) == expected_best_strategies
    # But "a" takes us to the final state, and "b" doesn't.
    # After the pruning, "a" is the only strategy left.
    best_strategies_reachability = ["a"]
    expected_final_best_strategies = ["a"]
    player_one_node_0.prune_paths_reachability(best_strategies_reachability)
    assert player_one_node_0.get_best_strategies_total_rewards(
        state_list_w_player_one_at_start, FLOOR_) == expected_final_best_strategies


def test_player_one_get_best_strategies_total_rewards_b_biggest_reward_and_final(
        player_one_node_0, state_list_two_final_states):
    expected_best_strategies = ["b"]
    assert player_one_node_0.get_best_strategies_total_rewards(state_list_two_final_states, FLOOR_) == \
        expected_best_strategies


def test_player_one_get_best_strategies_total_rewards_eq_rewards(
        player_one_node_0, state_list_two_final_states_eq_rew):
    expected_best_strategies = ["a", "b"]
    assert player_one_node_0.get_best_strategies_total_rewards(
        state_list_two_final_states_eq_rew, FLOOR_) == expected_best_strategies


# ----------------------------------------PlayerTwo----------------------------------------#

def test_player_two_value_iteration_reach_min(player_two_node_0, state_list_w_player_two_at_start):
    reachability = player_two_node_0.value_iteration_reach(state_list_w_player_two_at_start)
    expected_reachability = 0
    assert reachability == expected_reachability


def test_player_two_value_iteration_rewards_min(
        player_two_node_0, state_list_w_player_two_at_start):
    total_rewards = player_two_node_0.value_iteration_rewards(state_list_w_player_two_at_start)
    expected_total_rewards = 3
    assert total_rewards == expected_total_rewards


def test_player_two_value_iteration_rewards_min_(
        player_two_node_0, state_list_w_player_two_at_start_lower_rewards):
    total_rewards = player_two_node_0.value_iteration_rewards(
        state_list_w_player_two_at_start_lower_rewards)
    expected_total_rewards = 2
    assert total_rewards == expected_total_rewards


# ----------------------------------------all players----------------------------------------#

# In one iteration the reachability is 0 for s0, but it will increase in the next iterations
def test_players_value_iteration_reach_full(node_s0, node_s3, node_s4, state_list_game_5_5):
    reachability_s0 = node_s0.value_iteration_reach(state_list_game_5_5)
    reachability_s3 = node_s3.value_iteration_reach(state_list_game_5_5)
    reachability_s4 = node_s4.value_iteration_reach(state_list_game_5_5)
    expected_reachability_s0 = 0
    expected_reachability_s3 = 1/2
    expected_reachability_s4 = 3/4
    assert reachability_s0 == expected_reachability_s0
    assert reachability_s3 == expected_reachability_s3
    assert reachability_s4 == expected_reachability_s4


# This are the results after one iteration,
# but the values will be the same in the next iterations for this case
def test_players_value_iteration_rewards_full(
        node_s0, node_s1, node_s2, node_s3, node_s4,
        node_s5_bad, node_s6_good, node_s7_bad,
        state_list_game_5_5):
    rewards_s0 = node_s0.value_iteration_rewards(state_list_game_5_5)
    rewards_s1 = node_s1.value_iteration_rewards(state_list_game_5_5)
    rewards_s2 = node_s2.value_iteration_rewards(state_list_game_5_5)
    rewards_s3 = node_s3.value_iteration_rewards(state_list_game_5_5)
    rewards_s4 = node_s4.value_iteration_rewards(state_list_game_5_5)
    rewards_s5 = node_s5_bad.value_iteration_rewards(state_list_game_5_5)
    rewards_s6 = node_s6_good.value_iteration_rewards(state_list_game_5_5)
    rewards_s7 = node_s7_bad.value_iteration_rewards(state_list_game_5_5)
    expected_rewards_s0 = 2
    expected_rewards_s1 = 2
    expected_rewards_s2 = 5/3
    expected_rewards_s3 = 0
    expected_rewards_s4 = 0
    expected_rewards_s5 = 0
    expected_rewards_s6 = 0
    expected_rewards_s7 = 0
    assert rewards_s0 == expected_rewards_s0
    assert rewards_s1 == expected_rewards_s1
    assert rewards_s2 == expected_rewards_s2
    assert rewards_s3 == expected_rewards_s3
    assert rewards_s4 == expected_rewards_s4
    assert rewards_s5 == expected_rewards_s5
    assert rewards_s6 == expected_rewards_s6
    assert rewards_s7 == expected_rewards_s7


# ----------------------------------------Solver----------------------------------------#

def test_solver_solve_reachability_game_5_5(
        state_list_game_5_5, transition_list_game_5_5, final_states_game_5_5):
    reachability_strategies = Solver(state_list_game_5_5).solve_reachability(
        transition_list_game_5_5, final_states_game_5_5, True)
    expected_reachability_strategies = [["beta"], ["x"], ["x"], None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_solver_solve_reachability_game_5_5_no_prune(
        state_list_game_5_5, transition_list_game_5_5, final_states_game_5_5):
    reachability_strategies = Solver(state_list_game_5_5).solve_reachability(
        transition_list_game_5_5, final_states_game_5_5, False)
    expected_reachability_strategies = [["beta"], ["x"], ["x"], None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_solver_solve_reachability_game_5_5_same_reach(
        state_list_game_5_5_same_reach, transition_list_game_5_5_same_reach,
        final_states_game_5_5_same_reach):
    reachability_strategies = Solver(state_list_game_5_5_same_reach).solve_reachability(
        transition_list_game_5_5_same_reach, final_states_game_5_5_same_reach, True)
    expected_reachability_strategies = [["alfa", "beta"], ["x"], ["x"], None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_solver_solve_reachability_game_5_5_same_reach_no_prune(
        state_list_game_5_5_same_reach, transition_list_game_5_5_same_reach,
        final_states_game_5_5_same_reach):
    reachability_strategies = Solver(state_list_game_5_5_same_reach).solve_reachability(
        transition_list_game_5_5_same_reach, final_states_game_5_5_same_reach, False)
    expected_reachability_strategies = [["alfa", "beta"], ["x"], ["x"], None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_solver_solve_reachability_no_final_states(state_list_no_final):
    final_states = []
    transition_list = [[(1, 1)], [(1, 1)], [(1, 2)]]
    with pytest.raises(ValueError) as e:
        Solver(state_list_no_final).solve_reachability(transition_list, final_states, True)
    assert str(e.value) == "There must be at least one final state to solve reachability."


def test_solver_value_iteration_reachability(state_list_game_5_5):
    reachable_states = [state.idx for state in state_list_game_5_5 if state.idx not in [5, 7]]

    Solver(state_list_game_5_5).value_iteration_reachability(reachable_states, True)

    expected_reach_probabilities = [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0]
    for state, expected_prob in zip(state_list_game_5_5, expected_reach_probabilities):
        assert state.reach_probability == expected_prob


def test_solver_get_reachability_strategies(state_list_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    reachability_strategies = Solver(state_list_game_5_5)._get_reachability_strategies()
    expected_reachability_strategies = [["beta"], ["x"], ["x"], None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_solver_prune_stochastich_game(state_list_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    reachability_strategies = [["beta"], None, None, None, None, None, None, None]
    Solver(state_list_game_5_5).prune_stochastich_game(reachability_strategies)
    expected_nodes_transitions = [[("beta", 2)], [], [("x", 4)], [],
                                  [(1, 6)], [], [(1, 6)], []]
    for state, expected_transitions in zip(state_list_game_5_5, expected_nodes_transitions):
        assert state.next_states == expected_transitions


def test_solver_prune_stochastich_game_2(state_list_redistrib):
    init_reachability(state_list_redistrib, [1/2, 0, 0, 1, 0, 1])
    reachability_strategies = [None, ["epsilon"], None, ["gamma"], None, None]
    Solver(state_list_redistrib).prune_stochastich_game(reachability_strategies)
    expected_nodes_transitions = [[(1, 5)], [], [], [("gamma", 5)], [], [(1, 5)]]
    for state, expected_transitions in zip(state_list_redistrib, expected_nodes_transitions):
        assert state.next_states == expected_transitions


def test_solver_prune_paths(state_list_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    reachability_strategies = [["beta"], None, None, None, None, None, None, None]
    solver = Solver(state_list_game_5_5)
    solver.prune_paths(reachability_strategies)
    expected_nodes_transitions = [[("beta", 2)], [("x", 3)], [("x", 4)],
                                  [(1, 6)], [(1, 6)], [], [(1, 6)], []]
    for state, expected_transitions in zip(state_list_game_5_5, expected_nodes_transitions):
        assert state.next_states == expected_transitions


def test_solver_prune_paths_2(state_list_redistrib):
    init_reachability(state_list_redistrib, [1/2, 0, 0, 1, 0, 1])
    reachability_strategies = [None, ["epsilon"], None, ["gamma"], None, None]
    solver = Solver(state_list_redistrib)
    solver.prune_paths(reachability_strategies)
    expected_nodes_transitions = [[(1, 5)], [], [("beta", 3), ("alfa", 4)],
                                  [("gamma", 5)], [], [(1, 5)]]
    for state, expected_transitions in zip(state_list_redistrib, expected_nodes_transitions):
        assert state.next_states == expected_transitions


def test_solver_prune_states(state_list_redistrib):
    init_reachability(state_list_redistrib, [1/2, 0, 0, 1, 0, 1])
    reachability_strategies = [None, ["epsilon"], None, ["gamma"], None, None]
    solver = Solver(state_list_redistrib)
    solver.prune_paths(reachability_strategies)
    solver.prune_states()
    expected_transitions = [[(1, 5)], [], [], [("gamma", 5)], [], [(1, 5)]]
    for state, expected_next_states in zip(state_list_redistrib, expected_transitions):
        assert state.next_states == expected_next_states


def test_solver_solve_total_rewards(
        state_list_game_5_5, transition_list_game_5_5, reachability_strategies_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    solver = Solver(state_list_game_5_5)
    total_rewards_strategies = solver.solve_total_rewards()
    # "alfa" has more rewards, so if we don't prune the states, "alfa" is the best strategy
    expected_total_rewards_strategies = [["alfa"], ["x"], ["x"], None, None, None, None, None]
    assert total_rewards_strategies == expected_total_rewards_strategies

    # but taking into account the conditional rewards, "beta" is better
    solver = Solver(state_list_game_5_5)
    solver.prune_stochastich_game(reachability_strategies_game_5_5)
    final_total_rewards_strategies = solver.solve_total_rewards()
    expected_final_total_rewards_strategies = [["beta"], [], ["x"], None, None, None, None, None]
    assert final_total_rewards_strategies == expected_final_total_rewards_strategies


def test_solver_solve_total_rewards_same_reach_alfa_better_rewards(
        state_list_game_5_5_same_reach, transition_list_game_5_5_same_reach,
        reachability_strategies_game_5_5_same_reach):
    init_reachability(state_list_game_5_5_same_reach, [1/2, 1/2, 1/2, 1/2, 1/2, 0, 1, 0])
    solver = Solver(state_list_game_5_5_same_reach)
    total_rewards_strategies = solver.solve_total_rewards()
    expected_total_rewards_strategies = [["alfa"], ["x"], ["x"], None, None, None, None, None]
    assert total_rewards_strategies == expected_total_rewards_strategies

    # as the reachability is the same for all the states,
    # there was no pruning. Also alfa has more rewards, so it is the best strategy
    solver = Solver(state_list_game_5_5_same_reach)
    solver.prune_stochastich_game(reachability_strategies_game_5_5_same_reach)
    final_total_rewards_strategies = solver.solve_total_rewards()
    expected_final_total_rewards_strategies = [["alfa"], ["x"], ["x"], None, None, None, None, None]
    assert final_total_rewards_strategies == expected_final_total_rewards_strategies


def test_solver_value_iteration_total_rewards(state_list_game_5_5):
    Solver(state_list_game_5_5).value_iteration_total_rewards()
    expected_rewards = [2, 2, 5/3, 0, 0, 0, 0, 0]
    for state, expected_rew in zip(state_list_game_5_5, expected_rewards):
        assert state.expected_rewards == expected_rew


def test_solver_get_total_rewards_strategies(state_list_game_5_5, reachability_strategies_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    solver = Solver(state_list_game_5_5)
    solver.value_iteration_total_rewards()
    total_rewards_strategies = solver._get_total_rewards_strategies()
    # "alfa" has more rewards, so if we don't prune the states, "alfa" is the best strategy
    expected_total_rewards_strategies = [["alfa"], ["x"], ["x"], None, None, None, None, None]
    assert total_rewards_strategies == expected_total_rewards_strategies

    # but taking into account the conditional rewards, "beta" is better
    solver = Solver(state_list_game_5_5)
    solver.value_iteration_total_rewards()
    solver.prune_stochastich_game(reachability_strategies_game_5_5)
    final_total_rewards_strategies = solver._get_total_rewards_strategies()
    expected_final_total_rewards_strategies = [["beta"], [], ["x"], None, None, None, None, None]
    assert final_total_rewards_strategies == expected_final_total_rewards_strategies
