from tad import StochasticGame
# import json
from example_games import GAMES

# NO se si es lo mejor usar JSON, no es bueno para las tuplas ni para las fracciones
# TODO hacer algo como time para ver cuanto tarda en resolver el juego
# TODO hacer un archivo de configuracion para los juegos
# TODO mandar resultados a un archivo de texto


def main():
    for name, game in GAMES.items():
        print("="*160)
        print()
        print(f"Running example: {name}")
        sgame = StochasticGame(**game)
        final_strategies, reachability_strategies = sgame.solve()
        print()
        print(f"Reachability strategies: {reachability_strategies}")
        print(f"Final strategies       : {final_strategies}")
        print()

 
if __name__ == "__main__":
    main()
