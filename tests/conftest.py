import pytest
from tad import (
    PLAYER_1,
    PLAYER_2,
    PlayerOne,
    PlayerTwo,
    PROBABILISTIC,
    ProbabilisticNode,
    StochasticGame,
    )


# ----------------------------------------------------------------------------#
# Simple graph with 3 probabilistic nodes,
# the first node points to the other two and the last one is final

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
# Graph with 3 nodes the first is a player_1 node
# and the other two are probabilistic, where the last one is final

@pytest.fixture
def player_one_node_0():
    player_one_node_0 = PlayerOne(
        player=PLAYER_1,
        idx=0,
        reward=1,
        next_states=[
            ("a", 1),
            ("b", 2),
        ],
        is_final_node=False,
    )
    return player_one_node_0


@pytest.fixture
def state_list_w_player_one_at_start(player_one_node_0, node_1_final, node_2):
    state_list = [player_one_node_0, node_1_final, node_2]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


@pytest.fixture
def player_two_node_0():
    player_two_node_0 = PlayerTwo(
        player=PLAYER_2,
        idx=0,
        reward=1,
        next_states=[
            ("a", 1),
            ("b", 2),
        ],
        is_final_node=False,
    )
    return player_two_node_0


@pytest.fixture
def state_list_w_player_two_at_start(player_two_node_0, node_1_final, node_2):
    state_list = [player_two_node_0, node_1_final, node_2]
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
def state_list_two_final_states(player_one_node_0, node_1_final, node_2_final):
    state_list = [player_one_node_0, node_1_final, node_2_final]
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
def state_list_two_final_states_eq_rew(player_one_node_0, node_1_final, node_2_final_eq_rew):
    state_list = [player_one_node_0, node_1_final, node_2_final_eq_rew]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


# ----------------------------------------------------------------------------#
# graph of figure 5.5 from the paper

@pytest.fixture
def node_s0():
    return PlayerOne(
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
    return PlayerTwo(
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
    return PlayerTwo(
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


@pytest.fixture
def state_list_game_5_5(
        node_s0, node_s1, node_s2, node_s3, node_s4, node_s5_bad, node_s6_good, node_s7_bad):
    state_list = [
        node_s0, node_s1, node_s2, node_s3, node_s4, node_s5_bad, node_s6_good, node_s7_bad]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


@pytest.fixture
def transition_matrix_game_5_5(state_list_game_5_5):
    return [
        [[('alfa', 1), ('beta', 2)], None, None, None, None, None, None, None],
        [None, [(' ', 3)], [(' ', 4)], None, None, None, None, None],
        [None, None, None, [(0.5, 5), (0.5, 6)], [(0.75, 6), (0.25, 7)], [(1, 5)],
         [(1, 6)], [(1, 7)]]
    ]
    # SI cambio la transition matrix por una lista de transiciones.
    # [
    # ("player 1", [('alfa', 1), ('beta', 2
    # ("player 2", [('x', 3)]),
    # ("player 2", [('z', 4)]),
    # ("probabilistic", [(0.5, 5), (0.5, 6)]),
    # ("probabilistic", [(0.75, 6), (0.25, 7)]),
    # ("probabilistic", [(1, 5)]),
    # ("probabilistic", [(1, 6)]),
    # ("probabilistic", [(1, 7)])
    # ]


@pytest.fixture
def final_states_game_5_5(node_s6_good):
    return [node_s6_good.idx]


@pytest.fixture
def reachability_strategies_game_5_5():
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
def state_list_game_5_5_same_reach(
        node_s0, node_s1, node_s2, node_s3, node_s4_eq_probs,
        node_s5_bad, node_s6_good, node_s7_bad):
    state_list = [
        node_s0, node_s1, node_s2, node_s3, node_s4_eq_probs,
        node_s5_bad, node_s6_good, node_s7_bad]
    for node in state_list:
        if node.is_final_node:
            node.reach_probability = 1
    return state_list


@pytest.fixture
def transition_matrix_game_5_5_same_reach(state_list_game_5_5_same_reach):
    return [
        [[('alfa', 1), ('beta', 2)], None, None, None, None, None, None, None],
        [None, [(' ', 3)], [(' ', 4)], None, None, None, None, None],
        [None, None, None, [(0.5, 5), (0.5, 6)], [(0.5, 6), (0.5, 7)], [(1, 5)], [(1, 6)], [(1, 7)]]
        ]


@pytest.fixture
def final_states_game_5_5_same_reach(node_s6_good):
    return [node_s6_good.idx]


@pytest.fixture
def reachability_strategies_game_5_5_same_reach():
    return [["alfa", "beta"], None, None, None, None, None, None, None]


# ----------------------------------------------------------------------------#
# graph of figure 5.5 from the paper, as a stochastic game

@pytest.fixture
def stochastic_game_game_5_5(transition_matrix_game_5_5, final_states_game_5_5):
    return StochasticGame(
        reward_list=[0, 2, 5/3, 0, 0, 0, 0, 0],
        final_states=final_states_game_5_5,
        transition_matrix=transition_matrix_game_5_5,
    )


@pytest.fixture
def stochastic_game_game_5_5_same_reach(
        transition_matrix_game_5_5_same_reach, final_states_game_5_5_same_reach):
    return StochasticGame(
        reward_list=[0, 2, 5/3, 0, 0, 0, 0, 0],
        final_states=final_states_game_5_5_same_reach,
        transition_matrix=transition_matrix_game_5_5_same_reach,
    )


# ----------------------------------------------------------------------------#
# Stochastic games with errors

@pytest.fixture
def stochastic_game_first_state_without_transitions():
    return StochasticGame(
        reward_list=[0, 0, 0],
        final_states=[],
        transition_matrix=[
            [None, None, None],
            [None, None, None],
            [None, [1, 2], [1, 2]],
            ],
    )


@pytest.fixture
def stochastic_game_incomplete_reward_list():
    return StochasticGame(
        reward_list=[0, 0],
        final_states=[2],
        transition_matrix=[
            [None, None, None],
            [None, None, None],
            [[1, 1], [1, 2], [1, 2]],
            ],
    )


@pytest.fixture
def stochastic_game_incomplete_player_one():
    return StochasticGame(
        reward_list=[0, 0, 0],
        final_states=[2],
        transition_matrix=[
            [None, None],
            [None, None, None],
            [[1, 1], [1, 2], [1, 2]],
            ],
    )


@pytest.fixture
def stochastic_game_incomplete_player_two():
    return StochasticGame(
        reward_list=[0, 0, 0],
        final_states=[2],
        transition_matrix=[
            [None, None, None],
            [None, None],
            [[1, 1], [1, 2], [1, 2]],
            ],
    )


@pytest.fixture
def stochastic_game_incomplete_probabilistic():
    return StochasticGame(
        reward_list=[0, 0, 0],
        final_states=[2],
        transition_matrix=[
            [None, None, [("a", 2)]],
            [None, None, None],
            [[1, 1], [1, 2]],
            ],
    )


@pytest.fixture
def stochastic_game_incomplete_transition_matrix():
    return StochasticGame(
        reward_list=[0, 0, 0],
        final_states=[2],
        transition_matrix=[
            [None, None, None],
            [[1, 1], [1, 2], [1, 2]],
            ],
    )
