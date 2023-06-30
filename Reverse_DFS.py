



def reverse_dfs_recursive(state, transitions, reachable_states, visited_states):
    reachable_states.append(state)
    visited_states.append(state)
    # TODO: los next state son los que llegan a state, mejorar la traniscion matrix
    for next_state in transitions[state]:
        if next_state not in visited_states:
            reverse_dfs_recursive(next_state, transitions, reachable_states, visited_states)


def reverse_dfs(transition_matrix, final_states):
    transitions = reverse_transition_matrix(transition_matrix) 
    reachable_states = []
    visited_states = []
    for final_state in final_states:
        reverse_dfs_recursive(final_state, transitions, reachable_states, visited_states)

    # remove final_states from reachable_states
    reachable_states = [state for state in reachable_states if state not in final_states]

    return reachable_states


def reverse_transition_matrix(transition_matrix):
    #transition matrix has 3 lists, one for each player
    # then for each player, if the state is in the list, then the state belongs to that player
    # the state is the index of the list
    # the value of the list is a list of the next states, that are tuples where the second element is the next state
    # and the first element is the probability of reaching that state or the action needed to reach that state.

    # To create the reversed matrix, we just need really a list, of tuples,
    # where the first element is the next state and the second is the state.
    reversed_transition_list = []

    for player in transition_matrix:
        for state in player:
            if state is not None:
                for next_state in state:
                    reversed_transition_list.append((next_state[1], state))

    # transfomr the list into a dict, where the key is the first element of the tuple and the value is a list of the second element of the tuple
    # TODO: CHECK IF THIS WORKS IN PYTHON
    # TODO: CHECK IF THIS WORKS IN PYTHON
    # TODO: CHECK IF THIS WORKS IN PYTHON
    # TODO: CHECK IF THIS WORKS IN PYTHON
    # TODO: CHECK IF THIS WORKS IN PYTHON
    # TODO: CHECK IF THIS WORKS IN PYTHON

    
    reversed_transition_list = dict(reversed_transition_list)

    return reversed_transition_list