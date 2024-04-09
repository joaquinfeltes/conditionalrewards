# Board:
#
#   [1|v( )] [4|v(X)] [0|<>( )] [2|v( )] [0|v( )]
#   [4|v( )] [2|v( )] [0|<>( )] [0|v(X)] [0|v(X)]
#   [0|<>(X)] [0|v( )] [0|v(X)] [0|<>( )] [1|v( )]
#   [2|<>(X)] [2|v( )] [0|<>( )] [0|<>( )] [2|<>( )]
#   [3|<>( )] [0|v( )] [3|<>( )] [3|<-( )] [1|v(X)]

{
 'game_a': {'rewards': [1, 4, 0, 2, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 2, 3, 0, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 25)],
                [('Green', 26)],
                [('Green', 27), ('Yellow', 52)],
                [('Green', 28)],
                [('Green', 29)],
                [('Green', 30)],
                [('Green', 31)],
                [('Green', 32), ('Yellow', 57)],
                [('Green', 33)],
                [('Green', 34)],
                [('Green', 35), ('Yellow', 60)],
                [('Green', 36)],
                [('Green', 37)],
                [('Green', 38), ('Yellow', 63)],
                [('Green', 39)],
                [('Green', 40), ('Yellow', 65)],
                [('Green', 41)],
                [('Green', 42), ('Yellow', 67)],
                [('Green', 43), ('Yellow', 68)],
                [('Green', 44), ('Yellow', 69)],
                [('Green', 45), ('Yellow', 70)],
                [('Green', 46)],
                [('Green', 47), ('Yellow', 72)],
                [('Green', 48), ('Yellow', 73)],
                [('Green', 49)],
                [('Down', 80)],
                [('Down', 81)],
                [('Down', 82)],
                [('Down', 83)],
                [('Down', 84)],
                [('Down', 85)],
                [('Down', 86)],
                [('Down', 87)],
                [('Down', 88)],
                [('Down', 89)],
                [('Down', 90)],
                [('Down', 91)],
                [('Down', 92)],
                [('Down', 93)],
                [('Down', 94)],
                [('Down', 95)],
                [('Down', 96)],
                [('Down', 97)],
                [('Down', 98)],
                [('Down', 99)],
                [('Down', 101)],
                [('Down', 101)],
                [('Down', 101)],
                [('Down', 101)],
                [('Down', 101)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 76), ('Right', 78)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 81), ('Right', 83)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 89), ('Right', 86)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 87), ('Right', 89)],
                [('Etha', 0)],
                [('Left', 94), ('Right', 91)],
                [('Etha', 0)],
                [('Left', 91), ('Right', 93)],
                [('Left', 92), ('Right', 94)],
                [('Left', 93), ('Right', 90)],
                [('Left', 99), ('Right', 96)],
                [('Etha', 0)],
                [('Left', 96), ('Right', 98)],
                [('Left', 97)],
                [('Etha', 0)],
                [(1, 0)],
                [(0.1, 100), (0.9, 1)],
                [(1, 2)],
                [(1, 3)],
                [(1, 4)],
                [(1, 5)],
                [(1, 6)],
                [(1, 7)],
                [(0.1, 100), (0.9, 8)],
                [(0.1, 100), (0.9, 9)],
                [(0.1, 100), (0.9, 10)],
                [(1, 11)],
                [(0.1, 100), (0.9, 12)],
                [(1, 13)],
                [(1, 14)],
                [(0.1, 100), (0.9, 15)],
                [(1, 16)],
                [(1, 17)],
                [(1, 18)],
                [(1, 19)],
                [(1, 20)],
                [(1, 21)],
                [(1, 22)],
                [(1, 23)],
                [(0.1, 100), (0.9, 24)],
                [(1, 100)],
                [(1, 101)]],
            'final_states': [101]},
 'game_b': {'rewards': [1, 4, 0, 2, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 2, 3, 0, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 25)],
                [('Green', 26)],
                [('Green', 27), ('Yellow', 52)],
                [('Green', 28)],
                [('Green', 29)],
                [('Green', 30)],
                [('Green', 31)],
                [('Green', 32), ('Yellow', 57)],
                [('Green', 33)],
                [('Green', 34)],
                [('Green', 35), ('Yellow', 60)],
                [('Green', 36)],
                [('Green', 37)],
                [('Green', 38), ('Yellow', 63)],
                [('Green', 39)],
                [('Green', 40), ('Yellow', 65)],
                [('Green', 41)],
                [('Green', 42), ('Yellow', 67)],
                [('Green', 43), ('Yellow', 68)],
                [('Green', 44), ('Yellow', 69)],
                [('Green', 45), ('Yellow', 70)],
                [('Green', 46)],
                [('Green', 47), ('Yellow', 72)],
                [('Green', 48), ('Yellow', 73)],
                [('Green', 49)],
                [('Down', 100)],
                [('Down', 101)],
                [('Down', 102)],
                [('Down', 103)],
                [('Down', 104)],
                [('Down', 105)],
                [('Down', 106)],
                [('Down', 107)],
                [('Down', 108)],
                [('Down', 109)],
                [('Down', 110)],
                [('Down', 111)],
                [('Down', 112)],
                [('Down', 113)],
                [('Down', 114)],
                [('Down', 115)],
                [('Down', 116)],
                [('Down', 117)],
                [('Down', 118)],
                [('Down', 119)],
                [('Down', 120)],
                [('Down', 121)],
                [('Down', 122)],
                [('Down', 123)],
                [('Down', 124)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 127), ('Right', 152)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 132), ('Right', 157)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 135), ('Right', 160)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 138), ('Right', 163)],
                [('Etha', 0)],
                [('Left', 140), ('Right', 165)],
                [('Etha', 0)],
                [('Left', 142), ('Right', 167)],
                [('Left', 143), ('Right', 168)],
                [('Left', 144), ('Right', 169)],
                [('Left', 145), ('Right', 170)],
                [('Etha', 0)],
                [('Left', 147), ('Right', 172)],
                [('Left', 148)],
                [('Etha', 0)],
                [(1, 0)],
                [(0.1, 175), (0.9, 1)],
                [(1, 2)],
                [(1, 3)],
                [(1, 4)],
                [(1, 5)],
                [(1, 6)],
                [(1, 7)],
                [(0.1, 175), (0.9, 8)],
                [(0.1, 175), (0.9, 9)],
                [(0.1, 175), (0.9, 10)],
                [(1, 11)],
                [(0.1, 175), (0.9, 12)],
                [(1, 13)],
                [(1, 14)],
                [(0.1, 175), (0.9, 15)],
                [(1, 16)],
                [(1, 17)],
                [(1, 18)],
                [(1, 19)],
                [(1, 20)],
                [(1, 21)],
                [(1, 22)],
                [(1, 23)],
                [(0.1, 175), (0.9, 24)],
                [(0.1, 75), (0.9, 80)],
                [(0.1, 76), (0.9, 81)],
                [(0.1, 77), (0.9, 82)],
                [(0.1, 78), (0.9, 83)],
                [(0.1, 79), (0.9, 84)],
                [(0.1, 80), (0.9, 85)],
                [(0.1, 81), (0.9, 86)],
                [(0.1, 82), (0.9, 87)],
                [(0.1, 83), (0.9, 88)],
                [(0.1, 84), (0.9, 89)],
                [(0.1, 85), (0.9, 90)],
                [(0.1, 86), (0.9, 91)],
                [(0.1, 87), (0.9, 92)],
                [(0.1, 88), (0.9, 93)],
                [(0.1, 89), (0.9, 94)],
                [(0.1, 90), (0.9, 95)],
                [(0.1, 91), (0.9, 96)],
                [(0.1, 92), (0.9, 97)],
                [(0.1, 93), (0.9, 98)],
                [(0.1, 94), (0.9, 99)],
                [(0.1, 95), (0.9, 176)],
                [(0.1, 96), (0.9, 176)],
                [(0.1, 97), (0.9, 176)],
                [(0.1, 98), (0.9, 176)],
                [(0.1, 99), (0.9, 176)],
                [(0.1, 75), (0.9, 79)],
                [(0.1, 76), (0.9, 75)],
                [(0.1, 77), (0.9, 76)],
                [(0.1, 78), (0.9, 77)],
                [(0.1, 79), (0.9, 78)],
                [(0.1, 80), (0.9, 84)],
                [(0.1, 81), (0.9, 80)],
                [(0.1, 82), (0.9, 81)],
                [(0.1, 83), (0.9, 82)],
                [(0.1, 84), (0.9, 83)],
                [(0.1, 85), (0.9, 89)],
                [(0.1, 86), (0.9, 85)],
                [(0.1, 87), (0.9, 86)],
                [(0.1, 88), (0.9, 87)],
                [(0.1, 89), (0.9, 88)],
                [(0.1, 90), (0.9, 94)],
                [(0.1, 91), (0.9, 90)],
                [(0.1, 92), (0.9, 91)],
                [(0.1, 93), (0.9, 92)],
                [(0.1, 94), (0.9, 93)],
                [(0.1, 95), (0.9, 99)],
                [(0.1, 96), (0.9, 95)],
                [(0.1, 97), (0.9, 96)],
                [(0.1, 98), (0.9, 97)],
                [(0.1, 99), (0.9, 98)],
                [(0.1, 75), (0.9, 76)],
                [(0.1, 76), (0.9, 77)],
                [(0.1, 77), (0.9, 78)],
                [(0.1, 78), (0.9, 79)],
                [(0.1, 79), (0.9, 75)],
                [(0.1, 80), (0.9, 81)],
                [(0.1, 81), (0.9, 82)],
                [(0.1, 82), (0.9, 83)],
                [(0.1, 83), (0.9, 84)],
                [(0.1, 84), (0.9, 80)],
                [(0.1, 85), (0.9, 86)],
                [(0.1, 86), (0.9, 87)],
                [(0.1, 87), (0.9, 88)],
                [(0.1, 88), (0.9, 89)],
                [(0.1, 89), (0.9, 85)],
                [(0.1, 90), (0.9, 91)],
                [(0.1, 91), (0.9, 92)],
                [(0.1, 92), (0.9, 93)],
                [(0.1, 93), (0.9, 94)],
                [(0.1, 94), (0.9, 90)],
                [(0.1, 95), (0.9, 96)],
                [(0.1, 96), (0.9, 97)],
                [(0.1, 97), (0.9, 98)],
                [(0.1, 98), (0.9, 99)],
                [(0.1, 99), (0.9, 95)],
                [(1, 175)],
                [(1, 176)]],
            'final_states': [176]},
 'game_c': {'rewards': [1, 4, 0, 2, 0, 4, 2, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 2, 3, 0, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 200)],
                [('Green', 201)],
                [('Green', 202), ('Yellow', 227)],
                [('Green', 203)],
                [('Green', 204)],
                [('Green', 205)],
                [('Green', 206)],
                [('Green', 207), ('Yellow', 232)],
                [('Green', 208)],
                [('Green', 209)],
                [('Green', 210), ('Yellow', 235)],
                [('Green', 211)],
                [('Green', 212)],
                [('Green', 213), ('Yellow', 238)],
                [('Green', 214)],
                [('Green', 215), ('Yellow', 240)],
                [('Green', 216)],
                [('Green', 217), ('Yellow', 242)],
                [('Green', 218), ('Yellow', 243)],
                [('Green', 219), ('Yellow', 244)],
                [('Green', 220), ('Yellow', 245)],
                [('Green', 221)],
                [('Green', 222), ('Yellow', 247)],
                [('Green', 223), ('Yellow', 248)],
                [('Green', 224)],
                [('Down', 125)],
                [('Down', 126)],
                [('Down', 127)],
                [('Down', 128)],
                [('Down', 129)],
                [('Down', 130)],
                [('Down', 131)],
                [('Down', 132)],
                [('Down', 133)],
                [('Down', 134)],
                [('Down', 135)],
                [('Down', 136)],
                [('Down', 137)],
                [('Down', 138)],
                [('Down', 139)],
                [('Down', 140)],
                [('Down', 141)],
                [('Down', 142)],
                [('Down', 143)],
                [('Down', 144)],
                [('Down', 145)],
                [('Down', 146)],
                [('Down', 147)],
                [('Down', 148)],
                [('Down', 149)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 152), ('Right', 177)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 157), ('Right', 182)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 160), ('Right', 185)],
                [('Etha', 0)],
                [('Etha', 0)],
                [('Left', 163), ('Right', 188)],
                [('Etha', 0)],
                [('Left', 165), ('Right', 190)],
                [('Etha', 0)],
                [('Left', 167), ('Right', 192)],
                [('Left', 168), ('Right', 193)],
                [('Left', 169), ('Right', 194)],
                [('Left', 170), ('Right', 195)],
                [('Etha', 0)],
                [('Left', 172), ('Right', 197)],
                [('Left', 173)],
                [('Etha', 0)],
                [('Down', 125)],
                [('Down', 126)],
                [('Down', 127), ('Left', 152), ('Right', 177)],
                [('Down', 128)],
                [('Down', 129)],
                [('Down', 130)],
                [('Down', 131)],
                [('Down', 132), ('Left', 157), ('Right', 182)],
                [('Down', 133)],
                [('Down', 134)],
                [('Down', 135), ('Left', 160), ('Right', 185)],
                [('Down', 136)],
                [('Down', 137)],
                [('Down', 138), ('Left', 163), ('Right', 188)],
                [('Down', 139)],
                [('Down', 140), ('Left', 165), ('Right', 190)],
                [('Down', 141)],
                [('Down', 142), ('Left', 167), ('Right', 192)],
                [('Down', 143), ('Left', 168), ('Right', 193)],
                [('Down', 144), ('Left', 169), ('Right', 194)],
                [('Down', 145), ('Left', 170), ('Right', 195)],
                [('Down', 146)],
                [('Down', 147), ('Left', 172), ('Right', 197)],
                [('Down', 148), ('Left', 173)],
                [('Down', 149)],
                [(1, 0)],
                [(0.1, 250), (0.9, 1)],
                [(1, 2)],
                [(1, 3)],
                [(1, 4)],
                [(1, 5)],
                [(1, 6)],
                [(1, 7)],
                [(0.1, 250), (0.9, 8)],
                [(0.1, 250), (0.9, 9)],
                [(0.1, 250), (0.9, 10)],
                [(1, 11)],
                [(0.1, 250), (0.9, 12)],
                [(1, 13)],
                [(1, 14)],
                [(0.1, 250), (0.9, 15)],
                [(1, 16)],
                [(1, 17)],
                [(1, 18)],
                [(1, 19)],
                [(1, 20)],
                [(1, 21)],
                [(1, 22)],
                [(1, 23)],
                [(0.1, 250), (0.9, 24)],
                [(0.1, 100), (0.9, 105)],
                [(0.1, 101), (0.9, 106)],
                [(0.1, 102), (0.9, 107)],
                [(0.1, 103), (0.9, 108)],
                [(0.1, 104), (0.9, 109)],
                [(0.1, 105), (0.9, 110)],
                [(0.1, 106), (0.9, 111)],
                [(0.1, 107), (0.9, 112)],
                [(0.1, 108), (0.9, 113)],
                [(0.1, 109), (0.9, 114)],
                [(0.1, 110), (0.9, 115)],
                [(0.1, 111), (0.9, 116)],
                [(0.1, 112), (0.9, 117)],
                [(0.1, 113), (0.9, 118)],
                [(0.1, 114), (0.9, 119)],
                [(0.1, 115), (0.9, 120)],
                [(0.1, 116), (0.9, 121)],
                [(0.1, 117), (0.9, 122)],
                [(0.1, 118), (0.9, 123)],
                [(0.1, 119), (0.9, 124)],
                [(0.1, 120), (0.9, 251)],
                [(0.1, 121), (0.9, 251)],
                [(0.1, 122), (0.9, 251)],
                [(0.1, 123), (0.9, 251)],
                [(0.1, 124), (0.9, 251)],
                [(0.1, 100), (0.9, 104)],
                [(0.1, 101), (0.9, 100)],
                [(0.1, 102), (0.9, 101)],
                [(0.1, 103), (0.9, 102)],
                [(0.1, 104), (0.9, 103)],
                [(0.1, 105), (0.9, 109)],
                [(0.1, 106), (0.9, 105)],
                [(0.1, 107), (0.9, 106)],
                [(0.1, 108), (0.9, 107)],
                [(0.1, 109), (0.9, 108)],
                [(0.1, 110), (0.9, 114)],
                [(0.1, 111), (0.9, 110)],
                [(0.1, 112), (0.9, 111)],
                [(0.1, 113), (0.9, 112)],
                [(0.1, 114), (0.9, 113)],
                [(0.1, 115), (0.9, 119)],
                [(0.1, 116), (0.9, 115)],
                [(0.1, 117), (0.9, 116)],
                [(0.1, 118), (0.9, 117)],
                [(0.1, 119), (0.9, 118)],
                [(0.1, 120), (0.9, 124)],
                [(0.1, 121), (0.9, 120)],
                [(0.1, 122), (0.9, 121)],
                [(0.1, 123), (0.9, 122)],
                [(0.1, 124), (0.9, 123)],
                [(0.1, 100), (0.9, 101)],
                [(0.1, 101), (0.9, 102)],
                [(0.1, 102), (0.9, 103)],
                [(0.1, 103), (0.9, 104)],
                [(0.1, 104), (0.9, 100)],
                [(0.1, 105), (0.9, 106)],
                [(0.1, 106), (0.9, 107)],
                [(0.1, 107), (0.9, 108)],
                [(0.1, 108), (0.9, 109)],
                [(0.1, 109), (0.9, 105)],
                [(0.1, 110), (0.9, 111)],
                [(0.1, 111), (0.9, 112)],
                [(0.1, 112), (0.9, 113)],
                [(0.1, 113), (0.9, 114)],
                [(0.1, 114), (0.9, 110)],
                [(0.1, 115), (0.9, 116)],
                [(0.1, 116), (0.9, 117)],
                [(0.1, 117), (0.9, 118)],
                [(0.1, 118), (0.9, 119)],
                [(0.1, 119), (0.9, 115)],
                [(0.1, 120), (0.9, 121)],
                [(0.1, 121), (0.9, 122)],
                [(0.1, 122), (0.9, 123)],
                [(0.1, 123), (0.9, 124)],
                [(0.1, 124), (0.9, 120)],
                [(0.1, 75), (0.9, 25)],
                [(0.1, 76), (0.9, 26)],
                [(0.1, 77), (0.9, 27)],
                [(0.1, 78), (0.9, 28)],
                [(0.1, 79), (0.9, 29)],
                [(0.1, 80), (0.9, 30)],
                [(0.1, 81), (0.9, 31)],
                [(0.1, 82), (0.9, 32)],
                [(0.1, 83), (0.9, 33)],
                [(0.1, 84), (0.9, 34)],
                [(0.1, 85), (0.9, 35)],
                [(0.1, 86), (0.9, 36)],
                [(0.1, 87), (0.9, 37)],
                [(0.1, 88), (0.9, 38)],
                [(0.1, 89), (0.9, 39)],
                [(0.1, 90), (0.9, 40)],
                [(0.1, 91), (0.9, 41)],
                [(0.1, 92), (0.9, 42)],
                [(0.1, 93), (0.9, 43)],
                [(0.1, 94), (0.9, 44)],
                [(0.1, 95), (0.9, 45)],
                [(0.1, 96), (0.9, 46)],
                [(0.1, 97), (0.9, 47)],
                [(0.1, 98), (0.9, 48)],
                [(0.1, 99), (0.9, 49)],
                [(0.1, 75), (0.9, 50)],
                [(0.1, 76), (0.9, 51)],
                [(0.1, 77), (0.9, 52)],
                [(0.1, 78), (0.9, 53)],
                [(0.1, 79), (0.9, 54)],
                [(0.1, 80), (0.9, 55)],
                [(0.1, 81), (0.9, 56)],
                [(0.1, 82), (0.9, 57)],
                [(0.1, 83), (0.9, 58)],
                [(0.1, 84), (0.9, 59)],
                [(0.1, 85), (0.9, 60)],
                [(0.1, 86), (0.9, 61)],
                [(0.1, 87), (0.9, 62)],
                [(0.1, 88), (0.9, 63)],
                [(0.1, 89), (0.9, 64)],
                [(0.1, 90), (0.9, 65)],
                [(0.1, 91), (0.9, 66)],
                [(0.1, 92), (0.9, 67)],
                [(0.1, 93), (0.9, 68)],
                [(0.1, 94), (0.9, 69)],
                [(0.1, 95), (0.9, 70)],
                [(0.1, 96), (0.9, 71)],
                [(0.1, 97), (0.9, 72)],
                [(0.1, 98), (0.9, 73)],
                [(0.1, 99), (0.9, 74)],
                [(1, 250)],
                [(1, 251)]],
            'final_states': [251]}
}