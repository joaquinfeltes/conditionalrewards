import pytest
from reverse_dfs import (
    list_of_tuples_to_dict_of_lists,
    reverse_transition_list_core,
    reverse_transition_list,
    reverse_dfs,
    )


# ------------------ test for list_of_tuples_to_dict_of_lists -----------------
@pytest.fixture
def list_of_tuples():
    return [(1, 99), (1, 98), (2, 97), (2, 96), (3, 95), (1, 90)]


def test_list_of_tuples_to_dict_of_lists(list_of_tuples):
    expected_dict_of_lists = {1: [99, 98, 90], 2: [97, 96], 3: [95]}
    dict_of_lists = list_of_tuples_to_dict_of_lists(list_of_tuples)
    assert dict_of_lists == expected_dict_of_lists
    assert type(dict_of_lists) == dict


# ------------------  test for reverse_transition_list_core ----------------------
@pytest.fixture
def transition_list():
    # from figure 5.4
    return [
        [("beta", 1), ("alfa", 2)],  [(3/4, 3), (1/4, 4)], [(1/2, 5), (1/2, 6)],
        [("delta", 4), ("gamma", 5)], [(1, 4)], [(1, 5)], [(1, 6)]
    ]


def test_reverse_transition_list_core(transition_list):
    reverse_transition_list = reverse_transition_list_core(transition_list)
    expected_reverse_transition_list = [
        (1, 0), (2, 0), (3, 1), (4, 1), (5, 2), (6, 2), (4, 3), (5, 3), (4, 4), (5, 5), (6, 6)
        ]
    assert reverse_transition_list == expected_reverse_transition_list
    assert type(reverse_transition_list) == list

# ------------------  test for reverse_transition_list ----------------------


def test_reverse_transition_list(transition_list):
    reversed_transitions = reverse_transition_list(transition_list)
    expected_reversed_transitions = {
        1: [0], 2: [0], 3: [1], 4: [1, 3, 4], 5: [2, 3, 5], 6: [2, 6], 0: []
        }
    assert reversed_transitions == expected_reversed_transitions
    assert type(reversed_transitions) == dict


# ------------------  test for reverse_dfs ------------------------------------
@pytest.fixture
def transition_list_state_two_can_not_reach_state_five():
    return [
        [("beta", 1), ("alfa", 2)],  [(3/4, 3), (1/4, 4)], [(1, 6)],
        [("delta", 4), ("gamma", 5)], [(1, 4)], [(1, 5)], [(1, 6)]
    ]


@pytest.fixture
def final_states():
    return [5]


def test_reverse_dfs(transition_list, final_states):
    reachable_states = reverse_dfs(transition_list, final_states)
    expected_reachable_states = [0, 1, 2, 3]
    assert sorted(reachable_states) == expected_reachable_states
    assert type(reachable_states) == list


def test_reverse_dfs_state_two_can_not_reach(
        transition_list_state_two_can_not_reach_state_five, final_states):
    reachable_states = reverse_dfs(
        transition_list_state_two_can_not_reach_state_five, final_states)
    expected_reachable_states = [0, 1, 3]
    assert sorted(reachable_states) == expected_reachable_states
