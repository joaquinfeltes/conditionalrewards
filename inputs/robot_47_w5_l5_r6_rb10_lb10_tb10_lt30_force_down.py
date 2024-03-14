# Board:
#
#   [3|->( )] [1|->( )] [0|<-( )] [6|<-( )] [0|v(X)]
#   [0|->(X)] [1|->(X)] [0|->( )] [0|->( )] [0|<>( )]
#   [2|<-(X)] [0|v( )] [0|<-( )] [2|->( )] [0|v( )]
#   [0|->( )] [1|->( )] [1|v( )] [0|->( )] [0|<>( )]
#   [1|<>(X)] [1|<>( )] [3|<-( )] [0|v( )] [0|<-( )]

{
 'game_a': {'rewards': [3, 1, 0, 6, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 25), ('Yellow', 50)],
                [('Green', 26), ('Yellow', 51)],
                [('Green', 27), ('Yellow', 52)],
                [('Green', 28), ('Yellow', 53)],
                [('Green', 29)],
                [('Green', 30), ('Yellow', 55)],
                [('Green', 31), ('Yellow', 56)],
                [('Green', 32), ('Yellow', 57)],
                [('Green', 33), ('Yellow', 58)],
                [('Green', 34), ('Yellow', 59)],
                [('Green', 35), ('Yellow', 60)],
                [('Green', 36)],
                [('Green', 37), ('Yellow', 62)],
                [('Green', 38), ('Yellow', 63)],
                [('Green', 39)],
                [('Green', 40), ('Yellow', 65)],
                [('Green', 41), ('Yellow', 66)],
                [('Green', 42)],
                [('Green', 43), ('Yellow', 68)],
                [('Green', 44), ('Yellow', 69)],
                [('Green', 45), ('Yellow', 70)],
                [('Green', 46), ('Yellow', 71)],
                [('Green', 47), ('Yellow', 72)],
                [('Green', 48)],
                [('Green', 49), ('Yellow', 74)],
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
                [('Right', 76)],
                [('Right', 77)],
                [('Left', 76)],
                [('Left', 77)],
                [('Etha', 0)],
                [('Right', 81)],
                [('Right', 82)],
                [('Right', 83)],
                [('Right', 84)],
                [('Left', 83), ('Right', 80)],
                [('Left', 89)],
                [('Etha', 0)],
                [('Left', 86)],
                [('Right', 89)],
                [('Etha', 0)],
                [('Right', 91)],
                [('Right', 92)],
                [('Etha', 0)],
                [('Right', 94)],
                [('Left', 93), ('Right', 90)],
                [('Left', 99), ('Right', 96)],
                [('Left', 95), ('Right', 97)],
                [('Left', 96)],
                [('Etha', 0)],
                [('Left', 98)],
                [(1, 0)],
                [(1, 1)],
                [(1, 2)],
                [(1, 3)],
                [(0.1, 100), (0.9, 4)],
                [(0.1, 100), (0.9, 5)],
                [(0.1, 100), (0.9, 6)],
                [(1, 7)],
                [(1, 8)],
                [(1, 9)],
                [(0.1, 100), (0.9, 10)],
                [(1, 11)],
                [(1, 12)],
                [(1, 13)],
                [(1, 14)],
                [(1, 15)],
                [(1, 16)],
                [(1, 17)],
                [(1, 18)],
                [(1, 19)],
                [(0.1, 100), (0.9, 20)],
                [(1, 21)],
                [(1, 22)],
                [(1, 23)],
                [(1, 24)],
                [(1, 100)],
                [(1, 101)]],
            'final_states': [101]},
 'game_b': {'rewards': [3, 1, 0, 6, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 25), ('Yellow', 50)],
                [('Green', 26), ('Yellow', 51)],
                [('Green', 27), ('Yellow', 52)],
                [('Green', 28), ('Yellow', 53)],
                [('Green', 29)],
                [('Green', 30), ('Yellow', 55)],
                [('Green', 31), ('Yellow', 56)],
                [('Green', 32), ('Yellow', 57)],
                [('Green', 33), ('Yellow', 58)],
                [('Green', 34), ('Yellow', 59)],
                [('Green', 35), ('Yellow', 60)],
                [('Green', 36)],
                [('Green', 37), ('Yellow', 62)],
                [('Green', 38), ('Yellow', 63)],
                [('Green', 39)],
                [('Green', 40), ('Yellow', 65)],
                [('Green', 41), ('Yellow', 66)],
                [('Green', 42)],
                [('Green', 43), ('Yellow', 68)],
                [('Green', 44), ('Yellow', 69)],
                [('Green', 45), ('Yellow', 70)],
                [('Green', 46), ('Yellow', 71)],
                [('Green', 47), ('Yellow', 72)],
                [('Green', 48)],
                [('Green', 49), ('Yellow', 74)],
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
                [('Right', 150)],
                [('Right', 151)],
                [('Left', 127)],
                [('Left', 128)],
                [('Etha', 0)],
                [('Right', 155)],
                [('Right', 156)],
                [('Right', 157)],
                [('Right', 158)],
                [('Left', 134), ('Right', 159)],
                [('Left', 135)],
                [('Etha', 0)],
                [('Left', 137)],
                [('Right', 163)],
                [('Etha', 0)],
                [('Right', 165)],
                [('Right', 166)],
                [('Etha', 0)],
                [('Right', 168)],
                [('Left', 144), ('Right', 169)],
                [('Left', 145), ('Right', 170)],
                [('Left', 146), ('Right', 171)],
                [('Left', 147)],
                [('Etha', 0)],
                [('Left', 149)],
                [(1, 0)],
                [(1, 1)],
                [(1, 2)],
                [(1, 3)],
                [(0.1, 175), (0.9, 4)],
                [(0.1, 175), (0.9, 5)],
                [(0.1, 175), (0.9, 6)],
                [(1, 7)],
                [(1, 8)],
                [(1, 9)],
                [(0.1, 175), (0.9, 10)],
                [(1, 11)],
                [(1, 12)],
                [(1, 13)],
                [(1, 14)],
                [(1, 15)],
                [(1, 16)],
                [(1, 17)],
                [(1, 18)],
                [(1, 19)],
                [(0.1, 175), (0.9, 20)],
                [(1, 21)],
                [(1, 22)],
                [(1, 23)],
                [(1, 24)],
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
 'game_c': {'rewards': [3, 1, 0, 6, 0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 0, 0, 1, 1, 0, 0, 1, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 200), ('Yellow', 225)],
                [('Green', 201), ('Yellow', 226)],
                [('Green', 202), ('Yellow', 227)],
                [('Green', 203), ('Yellow', 228)],
                [('Green', 204)],
                [('Green', 205), ('Yellow', 230)],
                [('Green', 206), ('Yellow', 231)],
                [('Green', 207), ('Yellow', 232)],
                [('Green', 208), ('Yellow', 233)],
                [('Green', 209), ('Yellow', 234)],
                [('Green', 210), ('Yellow', 235)],
                [('Green', 211)],
                [('Green', 212), ('Yellow', 237)],
                [('Green', 213), ('Yellow', 238)],
                [('Green', 214)],
                [('Green', 215), ('Yellow', 240)],
                [('Green', 216), ('Yellow', 241)],
                [('Green', 217)],
                [('Green', 218), ('Yellow', 243)],
                [('Green', 219), ('Yellow', 244)],
                [('Green', 220), ('Yellow', 245)],
                [('Green', 221), ('Yellow', 246)],
                [('Green', 222), ('Yellow', 247)],
                [('Green', 223)],
                [('Green', 224), ('Yellow', 249)],
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
                [('Right', 175)],
                [('Right', 176)],
                [('Left', 152)],
                [('Left', 153)],
                [('Etha', 0)],
                [('Right', 180)],
                [('Right', 181)],
                [('Right', 182)],
                [('Right', 183)],
                [('Left', 159), ('Right', 184)],
                [('Left', 160)],
                [('Etha', 0)],
                [('Left', 162)],
                [('Right', 188)],
                [('Etha', 0)],
                [('Right', 190)],
                [('Right', 191)],
                [('Etha', 0)],
                [('Right', 193)],
                [('Left', 169), ('Right', 194)],
                [('Left', 170), ('Right', 195)],
                [('Left', 171), ('Right', 196)],
                [('Left', 172)],
                [('Etha', 0)],
                [('Left', 174)],
                [('Down', 125), ('Right', 175)],
                [('Down', 126), ('Right', 176)],
                [('Down', 127), ('Left', 152)],
                [('Down', 128), ('Left', 153)],
                [('Down', 129)],
                [('Down', 130), ('Right', 180)],
                [('Down', 131), ('Right', 181)],
                [('Down', 132), ('Right', 182)],
                [('Down', 133), ('Right', 183)],
                [('Down', 134), ('Left', 159), ('Right', 184)],
                [('Down', 135), ('Left', 160)],
                [('Down', 136)],
                [('Down', 137), ('Left', 162)],
                [('Down', 138), ('Right', 188)],
                [('Down', 139)],
                [('Down', 140), ('Right', 190)],
                [('Down', 141), ('Right', 191)],
                [('Down', 142)],
                [('Down', 143), ('Right', 193)],
                [('Down', 144), ('Left', 169), ('Right', 194)],
                [('Down', 145), ('Left', 170), ('Right', 195)],
                [('Down', 146), ('Left', 171), ('Right', 196)],
                [('Down', 147), ('Left', 172)],
                [('Down', 148)],
                [('Down', 149), ('Left', 174)],
                [(1, 0)],
                [(1, 1)],
                [(1, 2)],
                [(1, 3)],
                [(0.1, 250), (0.9, 4)],
                [(0.1, 250), (0.9, 5)],
                [(0.1, 250), (0.9, 6)],
                [(1, 7)],
                [(1, 8)],
                [(1, 9)],
                [(0.1, 250), (0.9, 10)],
                [(1, 11)],
                [(1, 12)],
                [(1, 13)],
                [(1, 14)],
                [(1, 15)],
                [(1, 16)],
                [(1, 17)],
                [(1, 18)],
                [(1, 19)],
                [(0.1, 250), (0.9, 20)],
                [(1, 21)],
                [(1, 22)],
                [(1, 23)],
                [(1, 24)],
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
