# This file contains the functions needed to perform a reverse dfs on a transition matrix

def reverse_dfs(transition_list: list, final_states: list) -> list:
    transitions = reverse_transition_list(transition_list)
    reachable_states = []
    for final_state in final_states:
        reachable_states = reverse_dfs_recursive(final_state, transitions, reachable_states)

    reachable_states = [state for state in reachable_states if state not in final_states]
    reachable_states.sort()
    return reachable_states


def reverse_dfs_recursive(state: int, transitions: dict, reachable_states: list) -> list:
    rec_reachable_states = reachable_states.copy()
    rec_reachable_states.append(state)
    for next_state in transitions[state]:
        if next_state not in reachable_states:
            rec_reachable_states = reverse_dfs_recursive(
                next_state, transitions, rec_reachable_states)
    return rec_reachable_states


def reverse_transition_list(transition_list: list) -> dict:
    """
        The transition matrix has 3 lists, one for each player
        then for each player, if the state is not None in the list the state belongs to that player
        the name of the state is the index of the list
        the value of the element if is not None is a list of the next states,
        the next states are tuples where the first element is the probability of reaching
        that state or the action needed to reach that state.
        and the second element is the name of that state.
        The reversed transitions will be a dict with the key
        being the state and the value being a list of the states that can be reached
    """
    reversed_transition_list = reverse_transition_list_core(transition_list)
    reversed_transition_dict = list_of_tuples_to_dict_of_lists(reversed_transition_list)
    # The dict might miss some states, add them with empty lists
    reversed_transition_dict = add_missing_states(
        reversed_transition_dict, len(transition_list))
    return reversed_transition_dict


def reverse_transition_list_core(transition_list: list) -> list:
    reversed_transition_list = []
    for current_state, state_transitions in enumerate(transition_list):
        for _, next_state in state_transitions:
            reversed_transition_list.append((next_state, current_state))
    return reversed_transition_list


def list_of_tuples_to_dict_of_lists(list_of_tuples: list) -> dict:
    dict_of_lists = {}
    for _tuple in list_of_tuples:
        if _tuple[0] not in dict_of_lists:
            dict_of_lists[_tuple[0]] = []
        dict_of_lists[_tuple[0]].append(_tuple[1])
    return dict_of_lists


def add_missing_states(transition_dict: dict, number_of_states: int) -> dict:
    for state in range(number_of_states):
        if state not in transition_dict:
            transition_dict[state] = []
    return transition_dict
