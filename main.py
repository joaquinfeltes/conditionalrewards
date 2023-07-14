import time
from tad import StochasticGame
from example_games import GAMES


def save_results_to_file(name, reachability_strategies, final_strategies, total_time):
    with open(f"outputs/{name}.txt", "a") as file:
        file.write("="*160)
        file.write("\n")
        file.write(f"Running example: {name}\n")
        file.write(f"Reachability strategies: {reachability_strategies}\n")
        file.write(f"Final strategies       : {final_strategies}\n")
        file.write(f"Total time             : {total_time}\n")


def main():
    for name, game in GAMES.items():
        print("="*160)
        print()
        print(f"Running example: {name}")
        start = time.time()
        sgame = StochasticGame(**game)
        final_strategies, reachability_strategies = sgame.solve()
        end = time.time()
        total_time = end - start
        print()
        print(f"Reachability strategies: {reachability_strategies}")
        print(f"Final strategies       : {final_strategies}")
        print(f"Total time             : {total_time}")
        # save_results_to_file(name, reachability_strategies, final_strategies, total_time)


if __name__ == "__main__":
    main()
