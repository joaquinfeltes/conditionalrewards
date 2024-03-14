from roberta_generator import write_robots, prob_to_str

def get_max_from_matrix(matrix):
    return max([max(row) for row in matrix])

def create_sg_from_board(moves, rewards, loose_tiles,
                         prob_robot_break, prob_light_break, prob_tile_break):
    length = len(moves)
    width = len(moves[0])
    max_reward = get_max_from_matrix(rewards)
    max_move = get_max_from_matrix(moves)
    force_down = (max_move+1) == 4
    file_name = "inputs/manual_robot" + "_" + \
                "w" + str(width) + "_" + \
                "l" + str(length) + "_" + \
                "r" + str(max_reward) + "_" + \
                "rb" + prob_to_str(prob_robot_break) + "_" + \
                "lb" + prob_to_str(prob_light_break) + "_" + \
                "tb" + prob_to_str(prob_tile_break) + "_" +  \
                ("force_down" if force_down else "") + ".py"

    write_robots(file_name, length, width, moves, rewards, loose_tiles, prob_tile_break,
                prob_robot_break, prob_light_break)

