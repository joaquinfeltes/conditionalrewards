import pytest

from tad import (
    Node,
    PLAYER_1,
    PLAYER_2,
    PlayerNode,
    PROBABILISTIC,
    ProbabilisticNode,
    Solver,
    StochasticGame,
    )

from tests.node_fixtures import (
    node_0,
    node_1_final,
    node_2_final,
    node_2_final_eq_rew,
    node_2,
    node_s0,
    node_s1,
    node_s2,
    node_s3,
    node_s4,
    node_s5_bad,
    node_s6_good,
    node_s7_bad,
    player_node_0,
    state_list_simple,
    state_list_two_final_states,
    state_list_w_player_at_start,
    state_list_two_final_states_eq_rew,
    state_list_graph_5_5,
    transition_matrix_graph_5_5,
    final_states_graph_5_5,
    )
#----------------------------------------ProbabilisticNode----------------------------------------#
   
def test_probabilistic_node_is_loop_node_false():
    probabilistic_node_with_two_neighbors = ProbabilisticNode(
        player=PROBABILISTIC,
        idx=0,
        reward=0,
        next_states=[
            (0.5, 1),
            (0.5, 2),
        ],
        is_final_node=False,
    )
    assert probabilistic_node_with_two_neighbors.is_loop_node == False


def test_probabilistic_node_is_loop_node_false_2():
    probabilistic_node_with_one_neighboor = ProbabilisticNode(
        player=PROBABILISTIC,
        idx=0,
        reward=0,
        next_states=[
            (1, 1),
        ],
        is_final_node=False,
    )
    assert probabilistic_node_with_one_neighboor.is_loop_node == False


def test_probabilistic_node_is_loop_node_true():
    probabilistic_node_loop = ProbabilisticNode(
        player=PROBABILISTIC,
        idx=0,
        reward=0,
        next_states=[
            (1, 0),
            ],
        is_final_node=False,
    )
    assert probabilistic_node_loop.is_loop_node == True


def test_value_iteration_reach(node_0, state_list_simple):
    assert node_0.value_iteration_reach(state_list_simple) == 0.5



def test_value_iteration_rewards(node_0, state_list_simple):
    # At this moment we don't take into account if the state reaches a final state
    assert node_0.value_iteration_rewards(state_list_simple) == 3.5
    # If we take into account if the state reaches a final state
    # assert node_0.value_iteration_rewards(state_list_simple) == 1.75
    # no estoy seguro si la idea es que se multiplique ppor la probabilidad de llegar en cada
    # iteracion o si se multiplica por la probabilidad de llegar al final



#----------------------------------------PlayerNode----------------------------------------#

def test_player_node_get_next_state(player_node_0):
    expected_next_state_a = 1
    expected_next_state_b = 2
    assert player_node_0.get_next_state("a") == expected_next_state_a
    assert player_node_0.get_next_state("b") == expected_next_state_b


def test_player_node_get_best_strategies_reachability(player_node_0, state_list_w_player_at_start):
    expected_best_strategies = ["a"]
    assert player_node_0.get_best_strategies_reachability(state_list_w_player_at_start) == expected_best_strategies


def test_player_node_get_best_strategies_reachability_two_strategies(player_node_0, state_list_two_final_states):
    expected_best_strategies = ["a", "b"]
    assert player_node_0.get_best_strategies_reachability(state_list_two_final_states) == expected_best_strategies


def test_player_node_get_best_strategies_total_rewards(player_node_0, state_list_w_player_at_start):
    expected_best_strategies = ["a"]
    assert player_node_0.get_best_strategies_total_rewards(state_list_w_player_at_start) == expected_best_strategies


def test_player_node_get_best_strategies_total_rewards_b_biggest_reward_and_final(player_node_0, state_list_two_final_states):
    expected_best_strategies = ["b"]
    assert player_node_0.get_best_strategies_total_rewards(state_list_two_final_states) == expected_best_strategies


def test_player_node_get_best_strategies_total_rewards_eq_rewards(player_node_0, state_list_two_final_states_eq_rew):
    expected_best_strategies = ["a","b"]
    assert player_node_0.get_best_strategies_total_rewards(state_list_two_final_states_eq_rew) == expected_best_strategies


def test_player_node_prune_state(player_node_0):
    best_strategies = ["a"]
    assert player_node_0.next_states == [("a", 1), ("b", 2)]
    player_node_0.prune_state(best_strategies)
    assert player_node_0.next_states == [("a", 1)]


def test_player_node_value_iteration_reach_max(player_node_0, state_list_w_player_at_start):
    reachability = player_node_0.value_iteration_reach_max(state_list_w_player_at_start)
    expected_reachability = 1
    assert reachability == expected_reachability


# puedo hacer este test porque la clase player es la misma para player 1 o 2,
# pero en realidad esta funcion no se usa en el caso de player 1
def test_player_node_value_iteration_reach_min(player_node_0, state_list_w_player_at_start):
    reachability = player_node_0.value_iteration_reach_min(state_list_w_player_at_start)
    expected_reachability = 0
    assert reachability == expected_reachability


# in one iteration the reachability is 0, but it will increase in the next iterations
def test_player_node_value_iteration_reach_full(node_s0, node_s3, node_s4, state_list_graph_5_5):
    reachability_s0 = node_s0.value_iteration_reach_max(state_list_graph_5_5)
    reachability_s3 = node_s3.value_iteration_reach(state_list_graph_5_5)
    reachability_s4 = node_s4.value_iteration_reach(state_list_graph_5_5)
    expected_reachability_s0 = 0
    expected_reachability_s3 = 1/2
    expected_reachability_s4 = 1/2
    assert reachability_s0 == expected_reachability_s0
    assert reachability_s3 == expected_reachability_s3
    assert reachability_s4 == expected_reachability_s4


def test_player_node_value_iteration_rewards_max(player_node_0, state_list_w_player_at_start):
    total_rewards = player_node_0.value_iteration_rewards_max(state_list_w_player_at_start)
    expected_total_rewards = 4
    assert total_rewards == expected_total_rewards


def test_player_node_value_iteration_rewards_min(player_node_0, state_list_w_player_at_start):
    total_rewards = player_node_0.value_iteration_rewards_min(state_list_w_player_at_start)
    expected_total_rewards = 3
    assert total_rewards == expected_total_rewards


# This are the results after 1 iteration, but the values will be the same in the next iterations
def test_player_node_value_iteration_rewards_full(
        node_s0, node_s1, node_s2, node_s3, node_s4,
        node_s5_bad, node_s6_good, node_s7_bad, 
        state_list_graph_5_5):
    rewards_s0 = node_s0.value_iteration_rewards_max(state_list_graph_5_5)
    rewards_s1 = node_s1.value_iteration_rewards_min(state_list_graph_5_5)
    rewards_s2 = node_s2.value_iteration_rewards_min(state_list_graph_5_5)
    rewards_s3 = node_s3.value_iteration_rewards(state_list_graph_5_5)
    rewards_s4 = node_s4.value_iteration_rewards(state_list_graph_5_5)
    rewards_s5 = node_s5_bad.value_iteration_rewards(state_list_graph_5_5)
    rewards_s6 = node_s6_good.value_iteration_rewards(state_list_graph_5_5)
    rewards_s7 = node_s7_bad.value_iteration_rewards(state_list_graph_5_5)
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


def test_get_reachability_strategies():
    pass


def test_solve_reachability_graph_5_5(state_list_graph_5_5, transition_matrix_graph_5_5, final_states_graph_5_5):
    reachability_strategies = Solver().solve_reachability(
            state_list=state_list_graph_5_5,
            transition_matrix=transition_matrix_graph_5_5, 
            final_states=final_states_graph_5_5)
    expected_reachability_strategies = [["alfa", "beta"], None, None, None, None, None, None, None]
    assert reachability_strategies == expected_reachability_strategies


def test_get_total_rewards_strategies():
    pass


def test_solve_total_rewards():
    pass


#----------------------------------------StochasticGame----------------------------------------#

#TODO add a test to check that the idx is the same as the index in the list
#TODO add a test to check that the transition matrix is correct with the function from node_fixtures.py

def test_sg_init_states():
    pass


def test_sg_solve_reachability():
    pass

def test_sg_solve_total_rewards():
    pass

def test_solve_sg():
    pass
