import argparse
import logging
import time
from tad import StochasticGame


def save_results_to_file(game_resuts, file_name):
    file_name = file_name.split("/")[-1].split(".")[0]
    with open(f"outputs/{file_name}.txt", "w") as file:
        for name, game in game_resuts.items():
            reachability_strategies = game["reachability_strategies"]
            final_strategies = game["final_strategies"]
            total_time = game["total_time"]
            file.write("="*160)
            file.write(f"\nRunning example         : {name}\n")
            file.write(f"Reachability strategies : {reachability_strategies}\n")
            file.write(f"Final strategies        : {final_strategies}\n")
            file.write(f"Are equal               : {reachability_strategies == final_strategies}\n")
            file.write(f"Message                 : {game['msg']}\n")
            file.write(f"Total time              : {total_time}\n")


def read_dict_from_file(file_name):
    with open(file_name, 'r') as file:
        contents = file.read()
        dictionary = eval(contents)
        if not isinstance(dictionary, dict):
            raise ValueError("The file content is not a valid Python dictionary.")
        return dictionary


def run_games(games_dict):
    game_results = {}
    for name, game in games_dict.items():
        logging.info("\n" + "="*160 + "\n")
        logging.info(f"Running example: {name}")
        start = time.time()
        sgame = StochasticGame(**game)
        msg = "Game solved"
        try:
            final_strategies, reachability_strategies = sgame.solve()
        except ValueError as e:
            logging.error(f"Error while solving the game: {e}")
            reachability_strategies = None
            final_strategies = None
            msg = f"Error while solving the game: {e}"
        end = time.time()
        total_time = end - start
        logging.info(f"\nReachability strategies: {reachability_strategies}")
        logging.info(f"Final strategies       : {final_strategies}")
        logging.info(f"Total time             : {total_time}")
        game_results[name] = {
            "reachability_strategies": reachability_strategies,
            "final_strategies": final_strategies,
            "total_time": total_time,
            "msg": msg
        }
    return game_results


def set_logger(level=logging.INFO):
    # import ipdb; ipdb.set_trace()
    if not level:
        return None
    if level == "INFO" or level == "i":
        logging.basicConfig(level=logging.INFO, format="%(message)s")
    elif level == "DEBUG" or level == "d":
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    elif level == "FULL_DEBUG" or level == "dd":
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        raise ValueError("Invalid log level. Choose between INFO and DEBUG.")


def init_parser():
    parser = argparse.ArgumentParser(
        prog="main.py",
        description=(
            "Run the solver for the stochastic games of an input file.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    logger_help = "Logger level. Choose between INFO (i), DEBUG (d) and FULL_DEBUG (dd)."
    save_help = "Save results to a file with the same name as the input file in the outputs folder."
    parser.add_argument('--file', '-f', type=str, required=True, help="Input file.")
    parser.add_argument('--log_level', '-l', type=str,
                        required=False, default=None, help=logger_help)
    parser.add_argument('--save_results', '-s', action="store_true", help=save_help)
    return parser


def main():
    parser = init_parser()
    parsed_args = parser.parse_args()
    set_logger(parsed_args.log_level)
    my_dict = read_dict_from_file(parsed_args.file)
    game_results = run_games(my_dict)
    if parsed_args.save_results:
        save_results_to_file(game_results, parsed_args.file)


if __name__ == "__main__":
    main()
