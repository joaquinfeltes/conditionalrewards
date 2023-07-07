import pytest
from reverse_dfs import list_of_tuples_to_dict_of_lists, reverse_transition_matrix_core, reverse_transition_matrix, reverse_dfs
from typing import List, Tuple, Dict



# ------------------ test for list_of_tuples_to_dict_of_lists -----------------
@pytest.fixture
def list_of_tuples():
    return [(1, 99), (1 , 98), (2, 97), (2, 96), (3, 95), (1, 90)]


def test_list_of_tuples_to_dict_of_lists(list_of_tuples):
    expected_dict_of_lists = {1: [99, 98, 90], 2: [97, 96], 3: [95]}
    dict_of_lists = list_of_tuples_to_dict_of_lists(list_of_tuples)
    assert dict_of_lists == expected_dict_of_lists
    assert type(dict_of_lists) == dict


# ------------------  test for reverse_transition_matrix_core ----------------------
@pytest.fixture
def transition_matrix():
    #from figure 5.4
    return [
        [[("beta", 1), ("alfa", 2)],  None,  None,  None,  None,  None,  None], 
        [None, None, None, [("delta", 4), ("gamma", 5)], None, None, None],
        [None, [(3/4, 3), (1/4, 4)], [(1/2, 5), (1/2, 6)], None, [(1, 4)], [(1, 5)], [(1, 6)]], 
    ]


def test_reverse_transition_matrix_core(transition_matrix):
    reverse_transition_list = reverse_transition_matrix_core(transition_matrix)
    expected_reverse_transition_list = [(1, 0), (2, 0), (4, 3), (5, 3), (3, 1), (4, 1), (5, 2), (6, 2), (4, 4), (5, 5), (6, 6)]
    assert reverse_transition_list == expected_reverse_transition_list
    assert type(reverse_transition_list) == list

# ------------------  test for reverse_transition_matrix ----------------------


def test_reverse_transition_matrix(transition_matrix):
    reversed_transitions = reverse_transition_matrix(transition_matrix)
    expected_reversed_transitions = {1: [0], 2: [0], 4: [3, 1, 4], 5: [3, 2, 5], 3: [1], 6: [2, 6], 0: []}
    assert reversed_transitions == expected_reversed_transitions
    assert type(reversed_transitions) == dict


# ------------------  test for reverse_dfs ------------------------------------
@pytest.fixture
def transition_matrix_state_two_can_not_reach_state_five():
    return [
        [[("beta", 1), ("alfa", 2)],  None,  None,  None,  None,  None,  None], 
        [None, None, None, [("delta", 4), ("gamma", 5)], None, None, None],
        [None, [(3/4, 3), (1/4, 4)], [(1, 6)], None, [(1, 4)], [(1, 5)], [(1, 6)]], 
    ]


@pytest.fixture
def final_states():
    return [5]


def test_reverse_dfs(transition_matrix, final_states):
    reachable_states = reverse_dfs(transition_matrix, final_states)
    expected_reachable_states = [0, 1, 2, 3]
    assert sorted(reachable_states) == expected_reachable_states
    assert type(reachable_states) == list
    

def test_reverse_dfs_state_two_can_not_reach(transition_matrix_state_two_can_not_reach_state_five, final_states):
    reachable_states = reverse_dfs(transition_matrix_state_two_can_not_reach_state_five, final_states)
    expected_reachable_states = [0, 1, 3]
    assert sorted(reachable_states) == expected_reachable_states
