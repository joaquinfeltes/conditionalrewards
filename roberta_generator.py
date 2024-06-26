import argparse
import random
import math


MOVE_SINTAX = ["<-", "<>", "->", "v"]
TILE_SYNTAX = ["( )", "(X)"]

FOUR_SPACES = "    "
EIGHT_SPACES = FOUR_SPACES + FOUR_SPACES
TWELVE_SPACES = EIGHT_SPACES + FOUR_SPACES
SIXTEEN_SPACES = TWELVE_SPACES + FOUR_SPACES


def gen_rnd_board(seed, length, width, prob_loose_tile, max_reward=6, force_down=False):
    moves = []
    rewards = []
    loose_tiles = []
    move_max = 4 if force_down else 3

    # construct the board
    random.seed(seed)
    for i in range(length):
        rewards.append([])
        loose_tiles.append([])
        for _ in range(width):
            rewards[i].append(math.floor(
                -math.log(
                    1.0/2.0**(max_reward+1) +
                    random.random()*(1.0-1.0/2.0**(max_reward+1)))/math.log(2.0)))
            loose_tiles[i].append(1 if random.random() < prob_loose_tile else 0)
    moves = get_random_moves(length, width, force_down)
    return moves, rewards, loose_tiles

def get_random_moves(length, width, force_down):
    moves = []
    for i in range(length):
        if force_down:
            moves.append(random.choices([0, 1, 2, 3], [0.1, 0.5, 0.1, 0.3], k=width))
            # force one of the moves to be down for each row
            move_down = random.randrange(0, width)
            moves[i][move_down] = 3
        else:
            moves.append(random.choices([0, 1, 2], [0.2, 0.6, 0.2], k=width))
    return moves

def player_two_transitions(length, width, moves, offset_r, offset_y):
    transition_list = []
    for i in range(length):
        for j in range(width):
            if moves[i][j] != 3:
                transition = [("Green", offset_r + i * width + j),  # To the player 1 down
                              ("Yellow", offset_y + i * width + j)]  # To the player 1 left right
            if moves[i][j] == 3:
                transition = [("Green", offset_r + i * width + j)]  # To the player 1 down
            transition_list.append(transition)
    return transition_list


def player_one_down_transitions(length, width, offset, winning_state=None):
    # Player 1 transitions for Green (going down)
    # they are sent to the corresponding prob state
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            if not winning_state:
                transition.append(("Down", offset + i * width + j))
            elif i < length - 1:
                transition.append(("Down", offset + i * width + j + width))
            else:
                transition.append(("Down", winning_state))
            transition_list.append(transition)
    return transition_list


def player_one_left_right_transitions(length, width, moves, offset_l, offset_r):
    # Player 1 transitions for Yellow (going left or right)
    # they are sent to the corresponding prob state
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            if offset_l != offset_r:
                transition.append(("Left",  offset_l + i * width + j))
                transition.append(("Right", offset_r + i * width + j))
            elif j == 0:
                transition.append(("Left",  offset_l + i * width + width - 1))
                transition.append(("Right", offset_r + i * width + j + 1))
            elif j == width - 1:
                transition.append(("Left",  offset_l + i * width + j - 1))
                transition.append(("Right", offset_r + i * width))
            else:
                transition.append(("Left",  offset_l + i * width + j - 1))
                transition.append(("Right", offset_r + i * width + j + 1))

            if moves[i][j] == 0:
                # just left
                transition_list.append([transition[0]])
            elif moves[i][j] == 1:
                # left and right
                transition_list.append(transition)
            elif moves[i][j] == 2:
                # just right
                transition_list.append([transition[1]])
            elif moves[i][j] == 3:
                # It should move down, so it shouldn't reach this state
                transition_list.append([("Etha", 0)])
    return transition_list


def prob_tile_break_transitions(length, width, prob_tile_break, loose_tiles, offset, loosing_state):
    # Probabilistic transitions (if the tile is loose,
    # there is a probability of break_prob of going to the bad state)
    # and there is a probability of 1 - break_prob of going to the proper tile,
    # meaning the same index for player 2
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            if loose_tiles[i][j] == 1:
                transition.append((prob_tile_break, loosing_state))
                transition.append((1 - prob_tile_break, offset + i * width + j))
            else:
                transition.append((1, offset + i * width + j))
            transition_list.append(transition)
    return transition_list


def write_preamble(my_file, length, width, moves, rewards, loose_tiles):
    # a depiction of the board as a comment
    my_file.write("# Board:\n#")
    for i in range(length):
        my_file.write("\n#  ")
        for j in range(width):
            my_file.write(" [" + str(int(rewards[i][j])) + "|" + MOVE_SINTAX[moves[i][j]] +
                          TILE_SYNTAX[loose_tiles[i][j]] + "]")
    my_file.write("\n\n")


def write_robot_A(my_file, length, width, moves, rewards, loose_tiles, prob_tile_break):
    # offsets for type of game A
    light = 0
    robot_down = 1
    robot_left_right = 2
    prob = 3
    total = 4

    n_prob_groups = 1
    n_robot_groups = 2

    n_tiles = length * width
    loosing_state = n_tiles * total
    winning_state = n_tiles * total + 1

    my_rewards = [reward for sublist in rewards for reward in sublist] + \
                 [0] * n_tiles * (total-1) + \
                 [0, 0]

    my_players = ["Player 2" for i in range(n_tiles)] + \
                 ["Player 1" for i in range(n_tiles*n_robot_groups)] + \
                 ["Probabilistic" for i in range(n_tiles*n_prob_groups)] + \
                 ["Probabilistic", "Probabilistic"]  # The bad and the good states

    my_final_states = [winning_state]

    transition_list = player_two_transitions(
        length, width, moves, offset_r=(robot_down*n_tiles), offset_y=(robot_left_right*n_tiles))

    transition_list += player_one_down_transitions(
        length, width, offset=(prob*n_tiles), winning_state=winning_state)

    transition_list += player_one_left_right_transitions(
        length, width, moves, offset_l=(prob*n_tiles), offset_r=(prob*n_tiles))

    transition_list += prob_tile_break_transitions(
        length, width, prob_tile_break, loose_tiles, offset=light, loosing_state=(loosing_state))

    # the bad and the good states are loops to themselves
    transition_list.append([(1, loosing_state)])
    transition_list.append([(1, winning_state)])

    game = {
        "rewards": my_rewards,
        "players": my_players,
        "transition_list": transition_list,
        "final_states": my_final_states
    }
    my_file.write("{\n 'game_a': ")

    my_file.write(str(game)
                  .replace("[[", "[\n[")
                  .replace("], ", "],\n")
                  .replace("[(", SIXTEEN_SPACES+"[(")
                  .replace("\n'", "\n" + TWELVE_SPACES + "'")
                  )
    my_file.write(",\n")


def prob_robot_down_break_transitions(length, width, prob_robot_break, offset, winning_state):
    # If it breaks has to go to the probabilistic state of the same tile
    # If it doesn't break, it goes down as it does normally
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            transition.append((prob_robot_break, offset + i * width + j))
            if i < length - 1:
                transition.append((1 - prob_robot_break, offset + i * width + j + width))
            else:
                transition.append((1 - prob_robot_break, winning_state))
            transition_list.append(transition)
    return transition_list


def prob_robot_left_break_transitions(length, width, prob_robot_break, offset):
    # If it breaks has to go to the probabilistic state of the same tile
    # If it doesn't break, it goes left as it does normally
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            transition.append((prob_robot_break, offset + i * width + j))
            if j == 0:
                transition.append((1 - prob_robot_break, offset + i * width + width - 1))
            else:
                transition.append((1 - prob_robot_break, offset + i * width + j - 1))
            transition_list.append(transition)
    return transition_list


def prob_robot_right_break_transitions(length, width, prob_robot_break, offset):
    # If it breaks has to go to the probabilistic state of the same tile
    # If it doesn't break, it goes right as it does normally
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            transition.append((prob_robot_break, offset + i * width + j))
            if j == width - 1:
                transition.append((1 - prob_robot_break, offset + i * width))
            else:
                transition.append((1 - prob_robot_break, offset + i * width + j + 1))
            transition_list.append(transition)
    return transition_list


def write_robot_B(my_file, length, width, moves, rewards, loose_tiles, prob_tile_break,
                  prob_robot_break):
    """
    The robot might break with probability prob_robot_break
    """

    # offsets for type of game B
    light = 0
    robot_down = 1
    robot_left_right = 2
    tile_break = 3
    robot_down_break = 4
    robot_left_break = 5
    robot_right_break = 6

    total = 7
    n_prob_groups = 4
    n_robot_groups = 2

    n_tiles = length * width
    loosing_state = n_tiles * total
    winning_state = n_tiles * total + 1

    my_rewards = [reward for sublist in rewards for reward in sublist] + \
                 [0] * n_tiles * (total-1) + \
                 [0, 0]

    my_players = ["Player 2" for i in range(n_tiles)] + \
                 ["Player 1" for i in range(n_tiles*n_robot_groups)] + \
                 ["Probabilistic" for i in range(n_tiles*n_prob_groups)] + \
                 ["Probabilistic", "Probabilistic"]

    my_final_states = [winning_state]

    # 0 light
    transition_list = player_two_transitions(
        length, width, moves, offset_r=(robot_down*n_tiles), offset_y=(robot_left_right*n_tiles))

    # 1 robot down -> prob robot down break
    transition_list += player_one_down_transitions(
        length, width, offset=(robot_down_break*n_tiles))

    # 2 robot left right
    transition_list += player_one_left_right_transitions(
        length, width, moves, offset_l=(robot_left_break*n_tiles),
        offset_r=(robot_right_break*n_tiles))

    # 3 tile break
    transition_list += prob_tile_break_transitions(
        length, width, prob_tile_break, loose_tiles, offset=light, loosing_state=(loosing_state))

    # 4 robot down break
    transition_list += prob_robot_down_break_transitions(
        length, width, prob_robot_break, offset=(tile_break*n_tiles), winning_state=winning_state)

    # 5 robot left break
    transition_list += prob_robot_left_break_transitions(
        length, width, prob_robot_break, offset=(tile_break*n_tiles))

    # 6 robot right break
    transition_list += prob_robot_right_break_transitions(
        length, width, prob_robot_break, offset=(tile_break*n_tiles))

    transition_list.append([(1, loosing_state)])
    transition_list.append([(1, winning_state)])

    game = {
        "rewards": my_rewards,
        "players": my_players,
        "transition_list": transition_list,
        "final_states": my_final_states
    }
    my_file.write(" 'game_b': ")

    my_file.write(str(game)
                  .replace("[[", "[\n[")
                  .replace("], ", "],\n")
                  .replace("[(", SIXTEEN_SPACES+"[(")
                  .replace("\n'", "\n" + TWELVE_SPACES + "'")
                  )
    my_file.write(",\n")


def player_one_down_left_right_transitions(length, width, moves, offset_d, offset_l, offset_r):
    """
    Player 1 transitions for when the light breaks
    the robot might break too, so the transitions go
    to the corresponding prob state
    """
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            transition.append(("Down", offset_d + i * width + j))
            transition.append(("Left",  offset_l + i * width + j))
            transition.append(("Right", offset_r + i * width + j))

            if moves[i][j] == 0:
                # without right
                transition_list.append([transition[0], transition[1]])
            elif moves[i][j] == 1:
                # all
                transition_list.append(transition)
            elif moves[i][j] == 2:
                # without left
                transition_list.append([transition[0], transition[2]])
            elif moves[i][j] == 3:
                # just down
                transition_list.append([transition[0]])
    return transition_list


def prob_light_break_transitions(length, width, prob_light_break, offset_ok, offset_break):
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            transition.append((prob_light_break, offset_break + i * width + j))
            transition.append((1 - prob_light_break, offset_ok + i * width + j))
            transition_list.append(transition)
    return transition_list


def write_robot_C(my_file, length, width, moves, rewards, loose_tiles, prob_tile_break,
                  prob_robot_break, prob_light_break):
    """
    The robot might break with probability prob_robot_break
    the light might break with probability prob_light_break
    """

    # offsets for type of game B
    light = 0
    robot_down = 1
    robot_left_right = 2
    robot_down_left_right = 3
    tile_break = 4
    robot_down_break = 5
    robot_left_break = 6
    robot_right_break = 7
    light_red_break = 8
    light_yellow_break = 9

    total = 10
    n_prob_groups = 6
    n_robot_groups = 3

    n_tiles = length * width
    loosing_state = n_tiles * total
    winning_state = n_tiles * total + 1

    my_rewards = [reward for sublist in rewards for reward in sublist] + \
                 [0] * n_tiles * (total-1) + \
                 [0, 0]

    my_players = ["Player 2" for i in range(n_tiles)] + \
                 ["Player 1" for i in range(n_tiles*n_robot_groups)] + \
                 ["Probabilistic" for i in range(n_tiles*n_prob_groups)] + \
                 ["Probabilistic", "Probabilistic"]

    my_final_states = [winning_state]

    # 0 light
    transition_list = player_two_transitions(
        length, width, moves, offset_r=(light_red_break*n_tiles), offset_y=(light_yellow_break*n_tiles))

    # 1 robot down
    transition_list += player_one_down_transitions(
        length, width, offset=(robot_down_break*n_tiles))

    # 2 robot left right
    transition_list += player_one_left_right_transitions(
        length, width, moves, offset_l=(robot_left_break*n_tiles),
        offset_r=(robot_right_break*n_tiles))

    # 3 robot down left right
    transition_list += player_one_down_left_right_transitions(
        length, width, moves, offset_d=(robot_down_break*n_tiles),
        offset_l=(robot_left_break*n_tiles), offset_r=(robot_right_break*n_tiles))

    # 4 tile break
    transition_list += prob_tile_break_transitions(
        length, width, prob_tile_break, loose_tiles, offset=light, loosing_state=(loosing_state))

    # 5 robot down break
    transition_list += prob_robot_down_break_transitions(
        length, width, prob_robot_break, offset=(tile_break*n_tiles), winning_state=winning_state)

    # 6 robot left break
    transition_list += prob_robot_left_break_transitions(
        length, width, prob_robot_break, offset=(tile_break*n_tiles))

    # 7 robot right break
    transition_list += prob_robot_right_break_transitions(
        length, width, prob_robot_break, offset=(tile_break*n_tiles))

    # 8 light Green break
    transition_list += prob_light_break_transitions(
        length, width, prob_light_break, offset_ok=(robot_down*n_tiles),
        offset_break=(robot_down_left_right*n_tiles))

    # 9 light Yellow break
    transition_list += prob_light_break_transitions(
        length, width, prob_light_break, offset_ok=(robot_left_right*n_tiles),
        offset_break=(robot_down_left_right*n_tiles))

    transition_list.append([(1, loosing_state)])
    transition_list.append([(1, winning_state)])

    game = {
        "rewards": my_rewards,
        "players": my_players,
        "transition_list": transition_list,
        "final_states": my_final_states
    }
    my_file.write(" 'game_c': ")

    my_file.write(str(game)
                  .replace("[[", "[\n[")
                  .replace("], ", "],\n")
                  .replace("[(", SIXTEEN_SPACES+"[(")
                  .replace("\n'", "\n" + TWELVE_SPACES + "'")
                  )
    my_file.write("\n}\n")


def write_robots(file_name, length, width, moves, rewards, loose_tiles, prob_tile_break,
                 prob_robot_break, prob_light_break):

    my_file = open(file_name, "w")

    write_preamble(my_file, length, width, moves, rewards, loose_tiles)
    write_robot_A(my_file, length, width, moves, rewards, loose_tiles, prob_tile_break)
    write_robot_B(my_file, length, width, moves, rewards, loose_tiles, prob_tile_break,
                  prob_robot_break)
    write_robot_C(my_file, length, width, moves, rewards, loose_tiles, prob_tile_break,
                  prob_robot_break, prob_light_break)
    my_file.close()


def init_parser():
    parser = argparse.ArgumentParser(
        prog="roberta_generator.py",
        description=(
            "Creates an input file that contains a dictionary with 3 games.\n"
            "One where the robot and the light can NOT break,\n"
            "one where just the robot might break and\n"
            "one where the robot and the light might break.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    seed_help = "  Sets the seed for the pseudo-random number generator to SEED. SEED must" + \
                " be a non-negative integer (0 or higher) (default = 0)\n"
    width_help = "  Sets the width of the board to WIDTH. WIDTH must be a positive integer" + \
                 " (greater than 0) (default = 3)\n"
    length_help = "  Sets the length of the board to LENGTH. LENGTH must be a positive" + \
                  " integer (greater than 0) (default = 3)\n"
    prob_robot_help = "  Sets the failure probability of the robot to PROB_ROBOT_BREAK." + \
                      " PROB_ROBOT_BREAK must be a float" + \
                      " in the interval (0,1) (default = 0.1)\n"
    prob_light_help = "  Sets the failure probability of the light to PROB_LIGHT_BREAK." + \
                      " PROB_LIGHT_BREAK must be a float" + \
                      " in the interval (0,1) (default = 0.1)\n"
    prob_loose_tile_help = "  Sets the probability of a tile being loose to PROB_LOOSE_TILE." + \
                           " PROB_LOOSE_TILE must be a float" + \
                           " in the interval (0,1) (default = 0.3)\n"
    prob_tile_break_help = "  Sets the probability of a tile breaking to PROB_TILE_BREAK." + \
                           " PROB_TILE_BREAK must be a float" + \
                           " in the interval (0,1) (default = 0.1)\n"
    max_rewards_help = "  Sets the maximum reward to MAX_REWARD. MAX_REWARD must be a" + \
                       " positive integer (greater than 0) (default = 6)\n"
    force_down_help = "  If added, there can be tiles that only allow the robot to go down.\n"
    parser.add_argument('--seed', '-s', type=int, required=False, default=0, help=seed_help)
    parser.add_argument('--width', '-w', type=int, required=False, default=3, help=width_help)
    parser.add_argument('--length', '-l', type=int, required=False, default=3, help=length_help)
    parser.add_argument('--prob_robot_break', '-p', type=float, required=False, default=0.1,
                        help=prob_robot_help)
    parser.add_argument('--prob_light_break', '-q', type=float, required=False, default=0.1,
                        help=prob_light_help)
    parser.add_argument('--prob_tile_break', '-r', type=float, required=False, default=0.1,
                        help=prob_tile_break_help)
    parser.add_argument('--prob_loose_tile', '-t', type=float, required=False, default=0.3,
                        help=prob_loose_tile_help)
    parser.add_argument('--max_reward', '-m', type=int, required=False, default=6,
                        help=max_rewards_help)
    parser.add_argument('--force_down', '-f', action='store_true', required=False,
                        default=False, help=force_down_help)
    return parser


def check_input(seed, width, length, prob_robot_break, prob_light_break, prob_loose_tile,
                prob_tile_break, max_reward):
    if seed < 0:
        raise ValueError("The seed must be a nonnegative integer")
    if width <= 0:
        raise ValueError("The width must be a positive integer")
    if length <= 0:
        raise ValueError("The length must be a positive integer")
    if prob_robot_break <= 0 or prob_robot_break >= 1:
        raise ValueError("The failure probability of the robot must be a float in (0,1)")
    if prob_light_break <= 0 or prob_light_break >= 1:
        raise ValueError("The failure probability of the light must be a float in (0,1)")
    if prob_loose_tile <= 0 or prob_loose_tile >= 1:
        raise ValueError("The probability of a tile being loose must be a float in (0,1)")
    if prob_tile_break <= 0 or prob_tile_break >= 1:
        raise ValueError("The probability of a tile breaking must be a float in (0,1)")
    if max_reward <= 0:
        raise ValueError("The maximum reward must be a positive integer")


def prob_to_str(prob):
    return str(int(prob*100))


def main():
    parser = init_parser()
    parsed_args = parser.parse_args()

    seed = parsed_args.seed
    width = parsed_args.width
    length = parsed_args.length
    max_reward = parsed_args.max_reward
    prob_loose_tile = parsed_args.prob_loose_tile
    prob_tile_break = parsed_args.prob_tile_break
    prob_robot_break = parsed_args.prob_robot_break
    prob_light_break = parsed_args.prob_light_break
    force_down = parsed_args.force_down

    check_input(seed, width, length, prob_robot_break, prob_light_break, prob_loose_tile,
                prob_tile_break, max_reward)

    moves, rewards, loose_tiles = gen_rnd_board(
        seed, length, width, prob_loose_tile, max_reward, force_down)

    file_name = "inputs/robot_" + str(seed) + "_" + \
                "w" + str(width) + "_" + \
                "l" + str(length) + "_" + \
                "r" + str(max_reward) + "_" + \
                "rb" + prob_to_str(prob_robot_break) + "_" + \
                "lb" + prob_to_str(prob_light_break) + "_" + \
                "tb" + prob_to_str(prob_tile_break) + "_" +  \
                "lt" + prob_to_str(prob_loose_tile) + \
                ("_force_down" if force_down else "") + ".py"

    write_robots(file_name, length, width, moves, rewards, loose_tiles, prob_tile_break,
                 prob_robot_break, prob_light_break)


if __name__ == "__main__":
    main()
