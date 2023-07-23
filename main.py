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
        final_strategies, reachability_strategies = sgame.solve()
        end = time.time()
        total_time = end - start
        logging.info(f"\nReachability strategies: {reachability_strategies}")
        logging.info(f"Final strategies       : {final_strategies}")
        logging.info(f"Total time             : {total_time}")
        game_results[name] = {
            "reachability_strategies": reachability_strategies,
            "final_strategies": final_strategies,
            "total_time": total_time
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
        prog="Run the stochastic games solver",
        description=(
            "Run the solver for the stochastic games of an input file.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--file', '-f', type=str, required=True, help="Input file.")
    parser.add_argument('--log_level', '-l', type=str,
                        required=False, default=None, help="logger level.")
    parser.add_argument('--save_results', '-s', action="store_true", help="Save results to file.")
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
