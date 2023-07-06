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
    FIRST_PLAYER,
    SECOND_PLAYER,
    PROBABILISTIC_PLAYER, 
    )


# ----------------------------------------------------------------------------#
# Simple graph with 3 probabilistic nodes, the first one points to the other two
# and the second one is a final node 
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



# ----------------------------------------------------------------------------#
# Graph with 3 nodes one for player_1 and 2 probabilistic, one of them being a final node 
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


# ----------------------------------------------------------------------------#
# graph with 3 nodes one for player 1 and two final ones 

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


# ----------------------------------------------------------------------------#
# graph with 3 nodes one for player 1 and two final ones, with equal rewards 


@pytest.fixture
def node_2_final_eq_rew():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=2,
        reward=2,
        next_states=[
            (1, 2),
        ],
        is_final_node=True,
    )


@pytest.fixture
def state_list_two_final_states_eq_rew(player_node_0, node_1_final, node_2_final_eq_rew):
    state_list = [player_node_0, node_1_final, node_2_final_eq_rew]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list



# ----------------------------------------------------------------------------#
# graph of figure 5.5 from the paper

@pytest.fixture
def node_s0():
    return PlayerNode(
        player=PLAYER_1,
        idx=0,
        reward=0,
        next_states=[
            ("alfa", 1),
            ("beta", 2),
        ],
        is_final_node=False,
    )


@pytest.fixture
def node_s1():
    return PlayerNode(
        player=PLAYER_2,
        idx=1,
        reward=2,
        next_states=[
            (" ", 3),
        ],
        is_final_node=False,
    )


@pytest.fixture
def node_s2():
    return PlayerNode(
        player=PLAYER_2,
        idx=2,
        reward=5/3,
        next_states=[
            (" ", 4),
        ],
        is_final_node=False,
    )


@pytest.fixture
def node_s3():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=3,
        reward=0,
        next_states=[
            (1/2, 5),
            (1/2, 6),
        ],
        is_final_node=False,
    )

@pytest.fixture
def node_s4():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=4,
        reward=0,
        next_states=[
            (3/4, 6),
            (1/4, 7),
        ],
        is_final_node=False,
    )

@pytest.fixture
def node_s5_bad():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=5,
        reward=0,
        next_states=[
            (1, 5),
        ],
        is_final_node=False,
    )


@pytest.fixture
def node_s6_good():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=6,
        reward=0,
        next_states=[
            (1, 6),
        ],
        is_final_node=True,
    )


@pytest.fixture
def node_s7_bad():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=7,
        reward=0,
        next_states=[
            (1, 7),
        ],
        is_final_node=False,
    )


#TODO add a test to check that the idx is the same as the index in the list

@pytest.fixture
def state_list_graph_5_5(node_s0, node_s1, node_s2, node_s3, node_s4, node_s5_bad, node_s6_good, node_s7_bad):
    state_list = [node_s0, node_s1, node_s2, node_s3, node_s4, node_s5_bad, node_s6_good, node_s7_bad]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


def state_list_to_transition_matrix(state_list):
    transitions_player_1 = [None] * len(state_list)
    transitions_player_2 = [None] * len(state_list)
    transitions_probabilistic = [None] * len(state_list)
    for state in state_list:
        if state.player == PLAYER_1:
            transitions_player_1[state.idx] = state.next_states
        elif state.player == PLAYER_2:
            transitions_player_2[state.idx] = state.next_states
        elif state.player == PROBABILISTIC:
            transitions_probabilistic[state.idx] = state.next_states
    transition_matrix = [transitions_player_1, transitions_player_2, transitions_probabilistic]
    return transition_matrix

@pytest.fixture
def transition_matrix_graph_5_5(state_list_graph_5_5):
    return state_list_to_transition_matrix(state_list_graph_5_5)


@pytest.fixture
def final_states_graph_5_5(node_s6_good):
    return [node_s6_good.idx]

@pytest.fixture
def reachability_strategies_graph_5_5():
    return [["beta"], None, None, None, None, None, None, None]


# ----------------------------------------------------------------------------#
# graph of figure 5.5 from the paper, with a small modification
# now every transition for probabilistic nodes are 1/2

@pytest.fixture
def node_s4_eq_probs():
    return ProbabilisticNode(
        player=PROBABILISTIC,
        idx=4,
        reward=0,
        next_states=[
            (1/2, 6),
            (1/2, 7),
        ],
        is_final_node=False,
    )

@pytest.fixture
def state_list_graph_5_5_bis(node_s0, node_s1, node_s2, node_s3, node_s4_eq_probs, node_s5_bad, node_s6_good, node_s7_bad):
    state_list = [node_s0, node_s1, node_s2, node_s3, node_s4_eq_probs, node_s5_bad, node_s6_good, node_s7_bad]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


@pytest.fixture
def transition_matrix_graph_5_5_bis(state_list_graph_5_5_bis):
    return state_list_to_transition_matrix(state_list_graph_5_5_bis)


@pytest.fixture
def final_states_graph_5_5_bis(node_s6_good):
    return [node_s6_good.idx]


@pytest.fixture
def reachability_strategies_graph_5_5_bis():
    return [["alfa", "beta"], None, None, None, None, None, None, None]
