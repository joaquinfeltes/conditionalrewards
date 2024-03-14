{
    "big_reward_small_prob": {
        "rewards": [
            0,
            0, 0,
            10**25, 0, 1,
            0
            ],
        "players": [
            "Player 1",
            "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic", "Probabilistic",
            "Probabilistic",
        ],
        "transition_list": [
            [("alfa", 1), ("beta", 2)],
            [(0.01, 3), (0.99, 4)], [(0.01, 4), (0.99, 5)],
            [(1, 6)], [(1, 4)], [(1, 6)],
            [(1, 6)]
        ],
        "final_states": [6]
    },
    "diferencia_lexicografico": {
        "rewards": [
            0,
            5, 2,
            2, 10,
            0, 0            
            ],
        "players": [
            "Player 1",
            "Player 2", "Player 1",
            "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic"
        ],
        "transition_list": [
            [("alfa", 1), ("beta", 2)],
            [("gamma", 3), ("delta", 4)],
            [("epsilon", 4)],
            [(0.35, 5), (0.65, 6)],
            [(0.3, 5), (0.7, 6)],
            [(1, 5)],
            [(1, 6)]
        ],
        "final_states": [5]
    },
    "necesidad_de_rho": {
        "rewards": [0, 0, 100, 1, 0, 0, 0],
        "players": [
            "Player 2", "Probabilistic", "Probabilistic", "Player 1", "Probabilistic",
            "Probabilistic", "Probabilistic"],
        "transition_list": [
            [("beta", 1), ("alfa", 2)],
            [(1/4, 4), (3/4, 3)],
            [(1/2, 5), (1/2, 6)],
            [("delta", 4), ("gamma", 5)],
            [(1, 4)],
            [(1, 5)],
            [(1, 6)]
            ],
        "final_states": [5]
    },
    "condicionadavssincondicionfull": {
        "rewards": [
            0,
            0,
            2, 5/3, 11/6,
            0, 0, 0,
            0, 0, 0, 0],
        "players": [
            "Player 1",
            "Player 2",
            "Player 2", "Player 2", "Player 2",
            "Probabilistic", "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic",
        ],
        "transition_list": [
            [("gamma", 1), ("delta", 4)],
            [("alfa", 2), ("beta", 3)],
            [(" ", 5)], [(" ", 6)], [(" ", 7)],
            [(0.5, 8), (0.5, 9)], [(0.75, 9), (0.25, 10)], [(0.5, 11), (0.5, 10)],
            [(1, 8)], [(1, 9)], [(1, 10)], [(1, 11)]
        ],
        "final_states": [9, 11]
    },
    "condicionadavssincondicionfull_reversed_players": {
        "rewards": [
            0,
            0,
            2, 5/3, 11/6,
            0, 0, 0,
            0, 0, 0, 0, 0],
        "players": [
            "Player 2",
            "Player 1",
            "Player 1", "Player 1", "Player 1",
            "Probabilistic", "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic",
        ],
        "transition_list": [
            [("gamma", 1), ("delta", 4)],
            [("alfa", 2), ("beta", 3)],
            [("x", 5)], [("y", 6)], [("z", 7)],
            [(0.5, 8), (0.5, 9)], [(0.75, 9), (0.25, 10)], [(0.5, 11), (0.5, 12)],
            [(1, 8)], [(1, 9)], [(1, 10)], [(1, 11)], [(1, 12)]
        ],
        "final_states": [9, 11]
    },
    "condicionadavssincondicionfull_all_player_one": {
        "rewards": [
            0,
            0,
            2, 5/3, 11/6,
            0, 0, 0,
            0, 0, 0, 0, 0],
        "players": [
            "Player 1",
            "Player 1",
            "Player 1", "Player 1", "Player 1",
            "Probabilistic", "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic",
        ],
        "transition_list": [
            [("gamma", 1), ("delta", 4)],
            [("alfa", 2), ("beta", 3)],
            [("x", 5)], [("y", 6)], [("z", 7)],
            [(0.5, 8), (0.5, 9)], [(0.75, 9), (0.25, 10)], [(0.5, 11), (0.5, 12)],
            [(1, 8)], [(1, 9)], [(1, 10)], [(1, 11)], [(1, 12)]
        ],
        "final_states": [9, 11]
    },
    "condicionadavssincondicionfull_all_player_one_same_probs": {
        "rewards": [
            0,
            0,
            2, 5/3, 11/6,
            0, 0, 0,
            0, 0, 0, 0, 0],
        "players": [
            "Player 1",
            "Player 1",
            "Player 1", "Player 1", "Player 1",
            "Probabilistic", "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic",
        ],
        "transition_list": [
            [("gamma", 1), ("delta", 4)],
            [("alfa", 2), ("beta", 3)],
            [("x", 5)], [("y", 6)], [("z", 7)],
            [(0.5, 8), (0.5, 9)], [(0.5, 9), (0.5, 10)], [(0.5, 11), (0.5, 12)],
            [(1, 8)], [(1, 9)], [(1, 10)], [(1, 11)], [(1, 12)]
        ],
        "final_states": [9, 11]
    },
    "ejemplo_complejo_condicionada": {
        "rewards": [
            10,
            0, 5,
            5, 0, 0,
            0, 2,
            0, 0],
        "players": [
            "Player 1",
            "Probabilistic", "Player 2",
            "Player 1", "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic"],
        "transition_list": [
            [("alfa_1", 1), ("alfa_2", 2)],
            [(0.8, 3), (0.1, 0), (0.1, 8)],
            [("gamma_1", 4), ("gamma_2", 5)],
            [("beta_1", 6), ("beta_2", 7)],
            [(0.4, 9), (0.5, 0), (0.1, 8)],
            [(0.6, 9), (0.3, 2), (0.1, 8)],
            [(0.8, 9), (0.125, 0), (0.075, 8)],
            [(0.6, 9), (0.2, 3), (0.2, 8)],
            [(1, 8)],
            [(1, 9)]
            ],
        "final_states": [9]
    },
    "condicionadavssincondicionsimple": {
        "rewards": [0, 2, 5/3, 0, 0, 0, 0, 0],
        "players": [
            "Player 1", "Player 2", "Player 2", "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic", "Probabilistic"
        ],
        "transition_list": [
            [("alfa", 1), ("beta", 2)], [(" ", 3)], [(" ", 4)],
            [(0.5, 5), (0.5, 6)], [(0.75, 6), (0.25, 7)],
            [(1, 5)], [(1, 6)], [(1, 7)]
        ],
        "final_states": [6]
    },
}
