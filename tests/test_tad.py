import pytest

from tad import (
    PLAYER_1,
    PLAYER_2,
    PROBABILISTIC,
    Solver,
    )

#TODO: set fixtures instead of importing them
from tests.node_fixtures import *

#TODO: do test typing and type hints

def init_reachability(state_list, reach_probability_list):
    # Hardcode the reach probability to each state
    for state, reach_probability in zip(state_list, reach_probability_list):
        state.reach_probability = reach_probability

#----------------------------------------ProbabilisticNode----------------------------------------#

def test_value_iteration_reach(node_0, state_list_simple):
    assert node_0.value_iteration_reach(state_list_simple) == 0.5


def test_value_iteration_rewards(node_0, state_list_simple):
    # At this moment we don't take into account if the state reaches a final state
    assert node_0.value_iteration_rewards(state_list_simple) == 3.5
    # Do I have to init reachability?
    init_reachability(state_list_simple, [1/2, 1, 0])
    assert node_0.value_iteration_rewards(state_list_simple) == 3.5
    
    # recompensa condicionada:
    # If we take into account if the state reaches a final state
    # assert node_0.value_iteration_rewards(state_list_simple) == 1.75
    # no estoy seguro si la idea es que se multiplique ppor la probabilidad de llegar en cada
    # iteracion o si se multiplica por la probabilidad de llegar al final


#----------------------------------------PlayerNode----------------------------------------#

def test_player_node_get_best_strategies_reachability(player_one_node_0, state_list_w_player_one_at_start):
    expected_best_strategies = ["a"]
    assert player_one_node_0.get_best_strategies_reachability(state_list_w_player_one_at_start) == expected_best_strategies


def test_player_node_get_best_strategies_reachability_two_strategies(player_one_node_0, state_list_two_final_states):
    expected_best_strategies = ["a", "b"]
    assert player_one_node_0.get_best_strategies_reachability(state_list_two_final_states) == expected_best_strategies


def test_player_node_get_best_strategies_total_rewards(player_one_node_0, state_list_w_player_one_at_start):
    expected_best_strategies = ["a"]
    assert player_one_node_0.get_best_strategies_total_rewards(state_list_w_player_one_at_start) == expected_best_strategies


def test_player_node_get_best_strategies_total_rewards_b_biggest_reward_and_final(player_one_node_0, state_list_two_final_states):
    expected_best_strategies = ["b"]
    assert player_one_node_0.get_best_strategies_total_rewards(state_list_two_final_states) == expected_best_strategies


def test_player_node_get_best_strategies_total_rewards_eq_rewards(player_one_node_0, state_list_two_final_states_eq_rew):
    expected_best_strategies = ["a","b"]
    assert player_one_node_0.get_best_strategies_total_rewards(state_list_two_final_states_eq_rew) == expected_best_strategies


def test_player_node_prune_state(player_one_node_0):
    best_strategies = ["a"]
    assert player_one_node_0.next_states == [("a", 1), ("b", 2)]
    player_one_node_0.prune_state(best_strategies)
    assert player_one_node_0.next_states == [("a", 1)]


def test_player_node_value_iteration_reach_max(player_one_node_0, state_list_w_player_one_at_start):
    reachability = player_one_node_0.value_iteration_reach(state_list_w_player_one_at_start)
    expected_reachability = 1
    assert reachability == expected_reachability


def test_player_node_value_iteration_reach_min(player_two_node_0, state_list_w_player_two_at_start):
    reachability = player_two_node_0.value_iteration_reach(state_list_w_player_two_at_start)
    expected_reachability = 0
    assert reachability == expected_reachability


# in one iteration the reachability is 0 for s0, but it will increase in the next iterations
def test_player_node_value_iteration_reach_full(node_s0, node_s3, node_s4, state_list_game_5_5):
    reachability_s0 = node_s0.value_iteration_reach(state_list_game_5_5)
    reachability_s3 = node_s3.value_iteration_reach(state_list_game_5_5)
    reachability_s4 = node_s4.value_iteration_reach(state_list_game_5_5)
    expected_reachability_s0 = 0
    expected_reachability_s3 = 1/2
    expected_reachability_s4 = 3/4
    assert reachability_s0 == expected_reachability_s0
    assert reachability_s3 == expected_reachability_s3
    assert reachability_s4 == expected_reachability_s4


def test_player_node_value_iteration_rewards_max(player_one_node_0, state_list_w_player_one_at_start):
    total_rewards = player_one_node_0.value_iteration_rewards(state_list_w_player_one_at_start)
    expected_total_rewards = 4
    assert total_rewards == expected_total_rewards


def test_player_node_value_iteration_rewards_min(player_two_node_0, state_list_w_player_two_at_start):
    total_rewards = player_two_node_0.value_iteration_rewards(state_list_w_player_two_at_start)
    expected_total_rewards = 3
    assert total_rewards == expected_total_rewards


# This are the results after one iteration,
# but the values will be the same in the next iterations for this case
def test_player_node_value_iteration_rewards_full(
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


#----------------------------------------Solver----------------------------------------#

#TODO: add tests for value iteration reachability and total rewards and prune


def test_get_reachability_strategies(state_list_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    reachability_strategies = Solver(state_list_game_5_5)._get_reachability_strategies()
    expected_reachability_strategies = [["beta"], None, None, None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_solve_reachability_game_5_5(state_list_game_5_5, transition_matrix_game_5_5, final_states_game_5_5):
    reachability_strategies = Solver(state_list_game_5_5).solve_reachability(transition_matrix_game_5_5, final_states_game_5_5)
    expected_reachability_strategies = [["beta"], None, None, None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_solve_reachability_game_5_5_same_reach(state_list_game_5_5_same_reach, transition_matrix_game_5_5_same_reach, final_states_game_5_5_same_reach):
    reachability_strategies = Solver(state_list_game_5_5_same_reach).solve_reachability(transition_matrix_game_5_5_same_reach, final_states_game_5_5_same_reach)
    expected_reachability_strategies = [["alfa", "beta"], None, None, None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_get_total_rewards_strategies(state_list_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    total_rewards_strategies = Solver(state_list_game_5_5)._get_total_rewards_strategies()
    expected_total_rewards_strategies = [["beta"], None, None, None, None, None, None, None]
    assert total_rewards_strategies == expected_total_rewards_strategies


def test_solve_total_rewards(state_list_game_5_5, transition_matrix_game_5_5, reachability_strategies_game_5_5):
    init_reachability(state_list_game_5_5, [3/4, 1/2, 3/4, 1/2, 3/4, 0, 1, 0])
    #might need to prune before
    test_get_total_rewards_strategies = Solver(state_list_game_5_5).solve_total_rewards()
    expected_total_rewards_strategies = [["beta"], None, None, None, None, None, None, None]
    assert test_get_total_rewards_strategies == expected_total_rewards_strategies


def test_solve_total_rewards_same_reach_alfa_better_rewards(state_list_game_5_5_same_reach, transition_matrix_game_5_5_same_reach, reachability_strategies_game_5_5_same_reach):
    init_reachability(state_list_game_5_5_same_reach, [1/2, 1/2, 1/2, 1/2, 1/2, 0, 1, 0])
    test_get_total_rewards_strategies = Solver(state_list_game_5_5_same_reach).solve_total_rewards()
    expected_total_rewards_strategies = [["alfa"], None, None, None, None, None, None, None]
    assert test_get_total_rewards_strategies == expected_total_rewards_strategies


#----------------------------------------StochasticGame----------------------------------------#

def test_sg_init_states(stochastic_game_game_5_5, state_list_game_5_5):
    state_list = stochastic_game_game_5_5.init_states()
    for state, expected_state in zip(state_list, state_list_game_5_5):
            assert state == expected_state


def test_sg_solve(stochastic_game_game_5_5):
    final_strategies = stochastic_game_game_5_5.solve()
    expected_final_strategies = [["beta"], None, None, None, None, None, None, None]
    assert final_strategies == expected_final_strategies


def test_sg_solve_same_reach(stochastic_game_game_5_5_same_reach):
    final_strategies = stochastic_game_game_5_5_same_reach.solve()
    expected_final_strategies = [["alfa"], None, None, None, None, None, None, None]
    assert final_strategies == expected_final_strategies


def test_sg_init_states_fail(stochastic_game_first_state_without_transitions):
    with pytest.raises(ValueError) as e:
        stochastic_game_first_state_without_transitions.init_states()
    assert str(e.value) == "Transition for state 0 is not defined"


def test_sg_init_incomplete_reward_list(stochastic_game_incomplete_reward_list):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_reward_list.init_states()
    assert str(e.value) == "The reward list must have the same number of elements as states in the game."


def test_sg_init_incomplete_player_one(stochastic_game_incomplete_player_one):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_player_one.init_states()
    assert str(e.value) == "The transition matrix must have the same number of states for each player."


def test_sg_init_incomplete_player_two(stochastic_game_incomplete_player_two):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_player_two.init_states()
    assert str(e.value) == "The transition matrix must have the same number of states for each player."


def test_sg_init_incomplete_probabilistic(stochastic_game_incomplete_probabilistic):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_probabilistic.init_states()
    assert str(e.value) == "The transition matrix must have the same number of states for each player."


def test_sg_init_incomplete_transition_matrix(stochastic_game_incomplete_transition_matrix):
    with pytest.raises(ValueError) as e:
        stochastic_game_incomplete_transition_matrix.init_states()
    assert str(e.value) == "The transition matrix must have 3 elements, one for each player and one for the probabilistic nodes."
