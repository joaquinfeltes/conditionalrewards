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


@pytest.fixture
def node_0():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=0,
        reward=1,
        next_states=[
            (0.5, 1),
            (0.5, 2),
        ],
        is_final_node=False,
    )


@pytest.fixture
def node_1_final():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=1,
        reward=2,
        next_states=[
            (1, 1),
        ],
        is_final_node=True,
    )


@pytest.fixture
def node_2():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=2,
        reward=3,
        next_states=[
            (1, 2),
        ],
        is_final_node=False,
    )


@pytest.fixture
def state_list_simple(node_0, node_1_final, node_2):
    # init the reach_probabily field of the node 1, as it is a final node
    state_list = [node_0, node_1_final, node_2]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list



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
@pytest.fixture
def player_node_0():
    player_node_0 = PlayerNode(
        player=PLAYER_1,
        idx=0,
        reward=1,
        next_states=[
            ("a", 1),
            ("b", 2),
        ],
        is_final_node=False,
    )
    return player_node_0


@pytest.fixture
def state_list_w_player_at_start(player_node_0, node_1_final, node_2):
    # init the reach_probabily field of the node 1, as it is a final node
    state_list = [player_node_0, node_1_final, node_2]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


@pytest.fixture
def node_2_final():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=2,
        reward=3,
        next_states=[
            (1, 2),
        ],
        is_final_node=True,
    )


@pytest.fixture
def state_list_two_final_states(player_node_0, node_1_final, node_2_final):
    state_list = [player_node_0, node_1_final, node_2_final]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


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




def test_player_node_prune_state(player_node_0):
    best_strategies = ["a"]
    assert player_node_0.next_states == [("a", 1), ("b", 2)]
    player_node_0.prune_state(best_strategies)
    assert player_node_0.next_states == [("a", 1)]


def test_player_node_value_iteration_reach_max(player_node_0, state_list_w_player_at_start):
    pass


def test_player_node_value_iteration_reach_min(player_node_0, state_list_w_player_at_start):
    pass


def test_player_node_value_iteration_rewards_max(player_node_0, state_list_w_player_at_start):
    pass


def test_player_node_value_iteration_rewards_min(player_node_0, state_list_w_player_at_start):
    pass




#----------------------------------------Solver----------------------------------------#


def test_solver():
    pass

#----------------------------------------StochasticGame----------------------------------------#


def test_stochastic_game():
    pass
