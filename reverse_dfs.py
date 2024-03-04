# This file contains the functions needed to perform a reverse dfs on a transition matrix

def reverse_dfs(transition_list: list, final_states: list) -> list:
    """
    Input: 
        transition_list: list, the transitions of the game.
        final_states: list, the list of final states of the game.
    Output:
        states_reaching_final: list, the list of states that can reach the final states.
    """
    reversed_transitions = reverse_transition_list(transition_list)
    states_reaching_final = []
    for final_state in final_states:
        states_reaching_final = reverse_dfs_recursive(final_state, reversed_transitions, states_reaching_final)

    states_reaching_final = [state for state in states_reaching_final if state not in final_states]
    states_reaching_final.sort()
    return states_reaching_final


def reverse_dfs_recursive(state: int, reversed_transitions: dict, reaching_states: list) -> list:
    """
        Input:
            state: int, the state to start the reverse dfs
            reversed_transitions: dict, the reversed transition matrix
            reaching_states: list, the list of states that reach the input state
                                (or a final state) the list is here to not
                                duplicate the states that are already in the list.
        Output:
            rec_reaching_states: the list of states that reach the input state (or a final state)
    """
    rec_reaching_states = reaching_states.copy()
    rec_reaching_states.append(state)
    for next_state in reversed_transitions[state]:
        if next_state not in reaching_states:
            rec_reaching_states = reverse_dfs_recursive(
                next_state, reversed_transitions, rec_reaching_states)
    return rec_reaching_states


def reverse_transition_list(transition_list: list) -> dict:
    """
        Input:
            transition_list: list, the transitions of the game.
                Is a list of lists of tuples,
                every list is a state and every tuple within that is a transition.
                The first element of the tuple is either:
                    - the probability of reaching that state (if the player is probabilistic)
                    - the action needed to reach that state (if is either player 1 or player 2)
                and the second element is the name of the state for that transition.
        Output: 
            reversed_transition_dict: dict, the reversed transition matrix.
                Every key is a state, and the values are lists of the states
                that can reach the key state in one step.
    """
    reversed_transition_list = reverse_transition_list_core(transition_list)
    reversed_transition_dict = list_of_tuples_to_dict_of_lists(reversed_transition_list)
    reversed_transition_dict = add_missing_states(
        reversed_transition_dict, len(transition_list))
    return reversed_transition_dict



def reverse_transition_list_core(transition_list: list) -> list:
    """
        Input:
            transition_list: list, the transitions of the game.
        Output:
            reversed_transition_list: list of tuples of reversed transitions. 
            Every tuple represents a transition from a state to another,
            the first element is the state we are going to,
            the second element is the state we are coming from. 
            (The order is switched).
    """
    reversed_transition_list = []
    for current_state, state_transitions in enumerate(transition_list):
        for _, next_state in state_transitions:
            reversed_transition_list.append((next_state, current_state))
    return reversed_transition_list


def list_of_tuples_to_dict_of_lists(list_of_tuples: list) -> dict:
    """
        Input:
            reversed_transition_list: list of tuples of reversed transitions. 
        Output:
            dict_of_lists: dict, the reversed transition matrix.
            We are going to convert the list of tuples to a dict of lists.
            The keys of the dict are the states that we are going to, (the state to reach).
            The values are lists of the states that lead to that state in one step.
    """
    dict_of_lists = {}
    for _tuple in list_of_tuples:
        if _tuple[0] not in dict_of_lists:
            dict_of_lists[_tuple[0]] = []
        dict_of_lists[_tuple[0]].append(_tuple[1])
    return dict_of_lists


def add_missing_states(transition_dict: dict, number_of_states: int) -> dict:
    """
        Input:
            transition_dict: dict, the reversed transition matrix.
            number_of_states: int, the number of states of the game.
        Output:
            transition_dict: dict, the reversed transition matrix.
            We are going to add the missing states with empty lists as values.
            So the states that can't be reached from any other state will be 
            in the dict with an empty list as value.
    """
    for state in range(number_of_states):
        if state not in transition_dict:
            transition_dict[state] = []
    return transition_dict
