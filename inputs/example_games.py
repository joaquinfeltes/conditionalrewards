{
    "game_5_4": {
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
    "game_5_5": {
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
    "game_5_6": {
        "rewards": [
            0,
            0,
            2, 5/3, 11/6,
            0, 0, 0,
            0, 0, 0, 0, 0],
        "players": [
            "Player 2",
            "Player 1",
            "Player 2", "Player 2", "Player 2",
            "Probabilistic", "Probabilistic", "Probabilistic",
            "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic", "Probabilistic",
        ],
        "transition_list": [
            [("gamma", 1), ("delta", 4)],
            [("alfa", 2), ("beta", 3)],
            [(" ", 5)], [(" ", 6)], [(" ", 7)],
            [(0.5, 8), (0.5, 9)], [(0.75, 9), (0.25, 10)], [(0.5, 11), (0.5, 12)],
            [(1, 8)], [(1, 9)], [(1, 10)], [(1, 11)], [(1, 12)]
        ],
        "final_states": [9, 11]
    },
    "game_5_6_reversed_players": {
        "rewards": [
            0,
            0,
            2, 5/3, 11/6,
            0, 0, 0,
            0, 0, 0, 0, 0],
        "players": [
            "Player 1",
            "Player 2",
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
    "game_5_7": {
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
    "game_5_6_all_player_one": {
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
    "game_5_6_all_player_one_same_probs": {
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
}
