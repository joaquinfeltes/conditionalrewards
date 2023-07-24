#!/usr/bin/python

import sys
import getopt
import random
import math


MOVE_SINTAX = ["<-", "<>", "->"]
TILE_SYNTAX = ["( )", "(X)"]

FOUR_SPACES = "    "
EIGHT_SPACES = FOUR_SPACES + FOUR_SPACES
TWELVE_SPACES = EIGHT_SPACES + FOUR_SPACES
SIXTEEN_SPACES = TWELVE_SPACES + FOUR_SPACES


def gen_rnd_board(seed, length, width, prob_loose_tile, max_reward=6):
    moves = []
    rewards = []
    loose_tiles = []

    # construct the board
    random.seed(seed)
    for i in range(length):
        moves.append([])
        rewards.append([])
        loose_tiles.append([])
        for j in range(width):
            moves[i].append(random.randrange(0, 3))
            rewards[i].append(math.floor(
                -math.log(
                    1.0/2.0**(max_reward+1) +
                    random.random()*(1.0-1.0/2.0**(max_reward+1)))/math.log(2.0)))
            loose_tiles[i].append(1 if random.random() < prob_loose_tile else 0)

    return moves, rewards, loose_tiles


def player_two_transitions(length, width, offset_r, offset_y):
    # Puedo mandar siempre a un probabilista con prob 1
    # y si se puede romper le cambio la probabilidad y listo
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = [("Red", offset_r + i * width + j),  # para el primer grupo de player 1
                          ("Yellow", offset_y + i * width + j)]  # para el segundo grupo
            transition_list.append(transition)
    return transition_list


def player_one_down_transitions(length, width, offset, winning_state=None):
    # Player 1 transitions for red (going down)
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
    # Player 1 transitions for yellow (going left or right)
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
        length, width, offset_r=(robot_down*n_tiles), offset_y=(robot_left_right*n_tiles))

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
    # tiene que llevar a los probabilistas de antes de la luz
    # si se rompe, va al del mismo estado en el que ya estaba
    # si no se rompe, va abajo como tocaba
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
    # tiene que llevar a los probabilistas de antes de la luz
    # si se rompe, va al del mismo estado en el que ya estaba
    # si no se rompe, va a izquierda como tocaba
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
    # tiene que llevar a los probabilistas de antes de la luz
    # si se rompe, va al del mismo estado en el que ya estaba
    # si no se rompe, va a derecha como tocaba
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
                 ["Probabilistic", "Probabilistic"]  # The bad and the good states

    my_final_states = [winning_state]

    # 0 light
    transition_list = player_two_transitions(
        length, width, offset_r=(robot_down*n_tiles), offset_y=(robot_left_right*n_tiles))

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

    # the bad and the good states are loops to themselves
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
                 ["Probabilistic", "Probabilistic"]  # The bad and the good states

    my_final_states = [winning_state]

    # 0 light
    transition_list = player_two_transitions(
        length, width, offset_r=(light_red_break*n_tiles), offset_y=(light_yellow_break*n_tiles))

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

    # 8 light red break
    transition_list += prob_light_break_transitions(
        length, width, prob_light_break, offset_ok=(robot_down*n_tiles),
        offset_break=(robot_down_left_right*n_tiles))

    # 9 light yellow break
    transition_list += prob_light_break_transitions(
        length, width, prob_light_break, offset_ok=(robot_left_right*n_tiles),
        offset_break=(robot_down_left_right*n_tiles))

    # the bad and the good states are loops to themselves
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


def usage(exit_val):
    print("\nusage robot_gen.py [-h] [-s <int> ] [-w <int>] [-l <int>] [-p <float>] [-q <float>]\n")
    print("-h :\n")
    print("  Print this help\n")
    print("-r :\n")
    print("  Exclude the rewards setting\n")
    print("-s num :\n")
    print("  Sets the seed for the pseudo-random number generator to 'num'. 'num' must be")
    print("  a non-negative integer (0 or higher) (default = 0)\n")
    print("-w num :\n")
    print("  Sets the width of the board to 'num'. 'num' must be a positive integer")
    print("  (greater than 0) (default = 5)\n")
    print("-l num :\n")
    print("  Sets the length of the board to 'num'. 'num' must be a positive integer")
    print("  (greater than 0) (default = 10)\n")
    print("-p num :\n")
    print("  Sets the failure probability of the robot to 'num'. 'num' must be a float")
    print("  in the interval (0,1) (default = 0.1)\n")
    print("-q num :\n")
    print("  Sets the failure probability of the light to 'num'. 'num' must be a float")
    print("  in the interval (0,1) (default = 0.05)\n")
    sys.exit(exit_val)


def main(argv):

    def prob_to_str(prob):
        return str(int(prob*100))

    seed = 0
    width = 5
    length = 10
    prob_robot_break = 0.1
    prob_light_break = 0.05
    include_rewards = True

    prob_loose_tile = 0.30
    prob_tile_break = 0.1
    max_reward = 6

    # TODO use argparse instead of getopt
    try:
        opts, _ = getopt.getopt(argv, "hs:w:l:p:q:r", [
            "seed=", "width=", "length=", "prob_fail_robot", "prob_fail_light"])
    except getopt.GetoptError:
        usage(2)
    for opt, arg in opts:
        if opt == '-h':
            usage(0)
        elif opt in ("-s", "seed="):
            try:
                seed = int(arg)
            except ValueError:
                print("The seed must be a nonnegative integer")
                sys.exit(2)
            if seed < 0:
                print("The seed must be a nonnegative integer")
                sys.exit(2)
        elif opt in ("-w", "width="):
            try:
                width = int(arg)
            except ValueError:
                print("The width must be a positive integer")
                sys.exit(2)
            if width <= 0:
                print("The width must be a positive integer")
                sys.exit(2)
        elif opt in ("-l", "length="):
            try:
                length = int(arg)
            except ValueError:
                print("The length must be a positive integer")
                sys.exit(2)
            if length <= 0:
                print("The length must be a positive integer")
                sys.exit(2)
        elif opt in ("-p", "prob_fail_robot="):
            try:
                prob_robot_break = float(arg)
            except ValueError:
                print("The failure probability of the robot must be a float in (0,1)")
                sys.exit(2)
            if prob_robot_break <= 0 or prob_robot_break >= 1:
                print("The failure probability of the robot must be a float in (0,1)")
                sys.exit(2)
        elif opt in ("-q", "prob_fail_light="):
            try:
                prob_light_break = float(arg)
            except ValueError:
                print("The failure probability of the light must be a float in (0,1)")
                sys.exit(2)
            if prob_light_break <= 0 or prob_light_break >= 1:
                print("The failure probability of the light must be a float in (0,1)")
                sys.exit(2)
        elif opt == "-r":
            include_rewards = False

    moves, rewards, loose_tiles = gen_rnd_board(
        seed, length, width, prob_loose_tile, max_reward)

    file_name = "inputs/robot_" + str(seed) + "_" + str(width) + "_" + str(length)+"_" + \
                prob_to_str(prob_robot_break) + "_" + prob_to_str(prob_light_break) + "_" + \
                prob_to_str(prob_loose_tile) + ".py"

    write_robots(file_name, length, width, moves, rewards, loose_tiles, prob_tile_break,
                 prob_robot_break, prob_light_break)


if __name__ == "__main__":
    main(sys.argv[1:])
