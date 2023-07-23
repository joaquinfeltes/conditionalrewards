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


# TODO Agregar los otros tipos de juego,
# es decir con errores en el semaforo o en el robot


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


def player_two_transitions(length, width, n_tiles):
    # Puedo mandar siempre a un probabilista con prob 1
    # y si se puede romper le cambio la probabilidad y listo
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = [("Red", n_tiles + i * width + j),  # para el primer grupo de player 1
                          ("Yellow", n_tiles * 2 + i * width + j)]  # para el segundo grupo
            transition_list.append(transition)
    return transition_list


def player_one_down_transitions(length, width, n_tiles):
    # Player 1 transitions for red (going down)
    # they are sent to the corresponding prob state
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            if i < length - 1:
                transition.append(("Down", (n_tiles * 3) + i * width + j + width))
            else:
                transition.append(("Down", n_tiles * 4 + 1))
            transition_list.append(transition)
    return transition_list


def player_one_left_right_transitions(length, width, n_tiles, moves):
    # Player 1 transitions for yellow (going left or right)
    # they are sent to the corresponding prob state
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            if j == 0:
                transition.append(("Left",  (n_tiles * 3) + i * width + width - 1))
                transition.append(("Right", (n_tiles * 3) + i * width + j + 1))
            elif j == width - 1:
                transition.append(("Left",  (n_tiles * 3) + i * width + j - 1))
                transition.append(("Right", (n_tiles * 3) + i * width))
            else:
                transition.append(("Left",  (n_tiles * 3) + i * width + j - 1))
                transition.append(("Right", (n_tiles * 3) + i * width + j + 1))

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


def prob_tile_break_transitions(length, width, n_tiles, prob_break, loose_tiles):
    # Probabilistic transitions (if the tile is loose,
    # there is a probability of break_prob of going to the bad state)
    # and there is a probability of 1 - break_prob of going to the proper tile,
    # meaning the same index for player 2
    transition_list = []
    for i in range(length):
        for j in range(width):
            transition = []
            if loose_tiles[i][j] == 1:
                transition.append((prob_break, n_tiles * 4))
                transition.append((1 - prob_break, i * width + j))
            else:
                transition.append((1, i * width + j))
            transition_list.append(transition)
    return transition_list


def write_preamble(file_name, length, width, moves, rewards, loose_tiles):
    # a depiction of the board as a comment
    # it will clean the file if it exists
    my_file = open(file_name, "w")
    my_file.write("# Board:\n#")
    for i in range(length):
        my_file.write("\n#  ")
        for j in range(width):
            my_file.write(" [" + str(int(rewards[i][j])) + "|" + MOVE_SINTAX[moves[i][j]] +
                          TILE_SYNTAX[loose_tiles[i][j]] + "]")
    my_file.write("\n\n")
    my_file.close()


def write_robot_A(file_name, length, width, moves, rewards, loose_tiles, prob_tile_break):
    n_tiles = length * width
    my_file = open(file_name, "a")

    my_rewards = [reward for sublist in rewards for reward in sublist] + \
                 [0] * n_tiles * 3 + \
                 [0, 0]
    my_players = ["Player 2" for i in range(n_tiles)] + \
                 ["Player 1" for i in range(n_tiles*2)] + \
                 ["Probabilistic" for i in range(n_tiles)] + \
                 ["Probabilistic", "Probabilistic"]  # The bad and the good states
    my_final_states = [n_tiles * 4 + 1]

    transition_list = player_two_transitions(length, width, n_tiles)
    transition_list += player_one_down_transitions(length, width, n_tiles)
    transition_list += player_one_left_right_transitions(length, width, n_tiles, moves)
    transition_list += prob_tile_break_transitions(
        length, width, n_tiles, prob_tile_break, loose_tiles)

    # the bad and the good states are loops to themselves
    transition_list.append([(1, n_tiles * 4)])
    transition_list.append([(1, n_tiles * 4 + 1)])

    game = {
        "rewards": my_rewards,
        "players": my_players,
        "transition_list": transition_list,
        "final_states": my_final_states
    }
    my_file.write("{'game_a': ")

    my_file.write(str(game)
                  .replace("[[", "[\n[")
                  .replace("], ", "],\n")
                  .replace("[(", SIXTEEN_SPACES+"[(")
                  .replace("\n'", "\n" + TWELVE_SPACES + "'")
                  )
    my_file.write(",\n")
    my_file.write("}\n")  # TODO this should be added only when is the last game
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

    seed = 0
    width = 5
    length = 10
    prob_robot = 0.1  # No lo uso
    prob_light = 0.05  # No lo uso
    include_rewards = True

    prob_loose_tile = 0.30
    prob_break = 0.1
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
                prob_robot = float(arg)
            except ValueError:
                print("The failure probability of the robot must be a float in (0,1)")
                sys.exit(2)
            if prob_robot <= 0 or prob_robot >= 1:
                print("The failure probability of the robot must be a float in (0,1)")
                sys.exit(2)
        elif opt in ("-q", "prob_fail_light="):
            try:
                prob_light = float(arg)
            except ValueError:
                print("The failure probability of the light must be a float in (0,1)")
                sys.exit(2)
            if prob_light <= 0 or prob_light >= 1:
                print("The failure probability of the light must be a float in (0,1)")
                sys.exit(2)
        elif opt == "-r":
            include_rewards = False

    moves, rewards, loose_tiles = gen_rnd_board(seed, length, width, prob_loose_tile, max_reward)

    file_name = (
                "inputs/robot_" + str(seed) + "_" + str(width) + "_" + str(length)+"_" +
                str(100*prob_robot)+"_"+str(100*prob_light)+"_"+str(100*prob_loose_tile) +
                ("" if include_rewards else "_NR")+".py"
                )
    write_preamble(file_name, length, width, moves, rewards, loose_tiles)
    write_robot_A(file_name, length, width, moves, rewards, loose_tiles, prob_break)


main(sys.argv[1:])
