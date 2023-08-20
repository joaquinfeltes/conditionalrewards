{
    "game_17_08": {
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
            [(0.8, 3), (0.1, 0), (0.1, 8)],  # p1 q1
            [("gamma_1", 4), ("gamma_2", 5)],
            [("beta_1", 6), ("beta_2", 7)],
            [(0.4, 9), (0.5, 0), (0.1, 8)],  # p4 q4
            [(0.6, 9), (0.3, 2), (0.1, 8)],  # p5 q5
            [(0.8, 9), (0.125, 0), (0.075, 8)],  # p2 q2
            [(0.6, 9), (0.2, 3), (0.2, 8)],  # p3 q3
            [(1, 8)],  # bad
            [(1, 9)]  # good
            ],
        "final_states": [9]
    }
}