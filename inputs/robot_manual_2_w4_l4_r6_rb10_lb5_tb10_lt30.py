# Board:
#
#   [0|<-( )] [5|->( )] [5|<-( )] [3|<-(X)]
#   [1|->( )] [0|<-( )] [0|<-(X)] [4|<>( )]
#   [5|->( )] [2|->( )] [0|<-( )] [0|<>( )]
#   [2|->( )] [0|<>( )] [0|->(X)] [0|->( )]

{
 'game_a': {'rewards': [0, 5, 5, 3, 1, 0, 0, 4, 5, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 16), ('Yellow', 32)],
                [('Green', 17), ('Yellow', 33)],
                [('Green', 18), ('Yellow', 34)],
                [('Green', 19), ('Yellow', 35)],
                [('Green', 20), ('Yellow', 36)],
                [('Green', 21), ('Yellow', 37)],
                [('Green', 22), ('Yellow', 38)],
                [('Green', 23), ('Yellow', 39)],
                [('Green', 24), ('Yellow', 40)],
                [('Green', 25), ('Yellow', 41)],
                [('Green', 26), ('Yellow', 42)],
                [('Green', 27), ('Yellow', 43)],
                [('Green', 28), ('Yellow', 44)],
                [('Green', 29), ('Yellow', 45)],
                [('Green', 30), ('Yellow', 46)],
                [('Green', 31), ('Yellow', 47)],
                [('Down', 52)],
                [('Down', 53)],
                [('Down', 54)],
                [('Down', 55)],
                [('Down', 56)],
                [('Down', 57)],
                [('Down', 58)],
                [('Down', 59)],
                [('Down', 60)],
                [('Down', 61)],
                [('Down', 62)],
                [('Down', 63)],
                [('Down', 65)],
                [('Down', 65)],
                [('Down', 65)],
                [('Down', 65)],
                [('Left', 51)],
                [('Right', 50)],
                [('Left', 49)],
                [('Left', 50)],
                [('Right', 53)],
                [('Left', 52)],
                [('Left', 53)],
                [('Left', 54), ('Right', 52)],
                [('Right', 57)],
                [('Right', 58)],
                [('Left', 57)],
                [('Left', 58), ('Right', 56)],
                [('Right', 61)],
                [('Left', 60), ('Right', 62)],
                [('Right', 63)],
                [('Right', 60)],
                [(1, 0)],
                [(1, 1)],
                [(1, 2)],
                [(0.1, 64), (0.9, 3)],
                [(1, 4)],
                [(1, 5)],
                [(0.1, 64), (0.9, 6)],
                [(1, 7)],
                [(1, 8)],
                [(1, 9)],
                [(1, 10)],
                [(1, 11)],
                [(1, 12)],
                [(1, 13)],
                [(0.1, 64), (0.9, 14)],
                [(1, 15)],
                [(1, 64)],
                [(1, 65)]],
            'final_states': [65]},
 'game_b': {'rewards': [0, 5, 5, 3, 1, 0, 0, 4, 5, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 16), ('Yellow', 32)],
                [('Green', 17), ('Yellow', 33)],
                [('Green', 18), ('Yellow', 34)],
                [('Green', 19), ('Yellow', 35)],
                [('Green', 20), ('Yellow', 36)],
                [('Green', 21), ('Yellow', 37)],
                [('Green', 22), ('Yellow', 38)],
                [('Green', 23), ('Yellow', 39)],
                [('Green', 24), ('Yellow', 40)],
                [('Green', 25), ('Yellow', 41)],
                [('Green', 26), ('Yellow', 42)],
                [('Green', 27), ('Yellow', 43)],
                [('Green', 28), ('Yellow', 44)],
                [('Green', 29), ('Yellow', 45)],
                [('Green', 30), ('Yellow', 46)],
                [('Green', 31), ('Yellow', 47)],
                [('Down', 64)],
                [('Down', 65)],
                [('Down', 66)],
                [('Down', 67)],
                [('Down', 68)],
                [('Down', 69)],
                [('Down', 70)],
                [('Down', 71)],
                [('Down', 72)],
                [('Down', 73)],
                [('Down', 74)],
                [('Down', 75)],
                [('Down', 76)],
                [('Down', 77)],
                [('Down', 78)],
                [('Down', 79)],
                [('Left', 80)],
                [('Right', 97)],
                [('Left', 82)],
                [('Left', 83)],
                [('Right', 100)],
                [('Left', 85)],
                [('Left', 86)],
                [('Left', 87), ('Right', 103)],
                [('Right', 104)],
                [('Right', 105)],
                [('Left', 90)],
                [('Left', 91), ('Right', 107)],
                [('Right', 108)],
                [('Left', 93), ('Right', 109)],
                [('Right', 110)],
                [('Right', 111)],
                [(1, 0)],
                [(1, 1)],
                [(1, 2)],
                [(0.1, 112), (0.9, 3)],
                [(1, 4)],
                [(1, 5)],
                [(0.1, 112), (0.9, 6)],
                [(1, 7)],
                [(1, 8)],
                [(1, 9)],
                [(1, 10)],
                [(1, 11)],
                [(1, 12)],
                [(1, 13)],
                [(0.1, 112), (0.9, 14)],
                [(1, 15)],
                [(0.1, 48), (0.9, 52)],
                [(0.1, 49), (0.9, 53)],
                [(0.1, 50), (0.9, 54)],
                [(0.1, 51), (0.9, 55)],
                [(0.1, 52), (0.9, 56)],
                [(0.1, 53), (0.9, 57)],
                [(0.1, 54), (0.9, 58)],
                [(0.1, 55), (0.9, 59)],
                [(0.1, 56), (0.9, 60)],
                [(0.1, 57), (0.9, 61)],
                [(0.1, 58), (0.9, 62)],
                [(0.1, 59), (0.9, 63)],
                [(0.1, 60), (0.9, 113)],
                [(0.1, 61), (0.9, 113)],
                [(0.1, 62), (0.9, 113)],
                [(0.1, 63), (0.9, 113)],
                [(0.1, 48), (0.9, 51)],
                [(0.1, 49), (0.9, 48)],
                [(0.1, 50), (0.9, 49)],
                [(0.1, 51), (0.9, 50)],
                [(0.1, 52), (0.9, 55)],
                [(0.1, 53), (0.9, 52)],
                [(0.1, 54), (0.9, 53)],
                [(0.1, 55), (0.9, 54)],
                [(0.1, 56), (0.9, 59)],
                [(0.1, 57), (0.9, 56)],
                [(0.1, 58), (0.9, 57)],
                [(0.1, 59), (0.9, 58)],
                [(0.1, 60), (0.9, 63)],
                [(0.1, 61), (0.9, 60)],
                [(0.1, 62), (0.9, 61)],
                [(0.1, 63), (0.9, 62)],
                [(0.1, 48), (0.9, 49)],
                [(0.1, 49), (0.9, 50)],
                [(0.1, 50), (0.9, 51)],
                [(0.1, 51), (0.9, 48)],
                [(0.1, 52), (0.9, 53)],
                [(0.1, 53), (0.9, 54)],
                [(0.1, 54), (0.9, 55)],
                [(0.1, 55), (0.9, 52)],
                [(0.1, 56), (0.9, 57)],
                [(0.1, 57), (0.9, 58)],
                [(0.1, 58), (0.9, 59)],
                [(0.1, 59), (0.9, 56)],
                [(0.1, 60), (0.9, 61)],
                [(0.1, 61), (0.9, 62)],
                [(0.1, 62), (0.9, 63)],
                [(0.1, 63), (0.9, 60)],
                [(1, 112)],
                [(1, 113)]],
            'final_states': [113]},
 'game_c': {'rewards': [0, 5, 5, 3, 1, 0, 0, 4, 5, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'players': ['Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 2', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Player 1', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic', 'Probabilistic'],
            'transition_list': [
                [('Green', 128), ('Yellow', 144)],
                [('Green', 129), ('Yellow', 145)],
                [('Green', 130), ('Yellow', 146)],
                [('Green', 131), ('Yellow', 147)],
                [('Green', 132), ('Yellow', 148)],
                [('Green', 133), ('Yellow', 149)],
                [('Green', 134), ('Yellow', 150)],
                [('Green', 135), ('Yellow', 151)],
                [('Green', 136), ('Yellow', 152)],
                [('Green', 137), ('Yellow', 153)],
                [('Green', 138), ('Yellow', 154)],
                [('Green', 139), ('Yellow', 155)],
                [('Green', 140), ('Yellow', 156)],
                [('Green', 141), ('Yellow', 157)],
                [('Green', 142), ('Yellow', 158)],
                [('Green', 143), ('Yellow', 159)],
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
                [('Left', 96)],
                [('Right', 113)],
                [('Left', 98)],
                [('Left', 99)],
                [('Right', 116)],
                [('Left', 101)],
                [('Left', 102)],
                [('Left', 103), ('Right', 119)],
                [('Right', 120)],
                [('Right', 121)],
                [('Left', 106)],
                [('Left', 107), ('Right', 123)],
                [('Right', 124)],
                [('Left', 109), ('Right', 125)],
                [('Right', 126)],
                [('Right', 127)],
                [('Down', 80), ('Left', 96)],
                [('Down', 81), ('Right', 113)],
                [('Down', 82), ('Left', 98)],
                [('Down', 83), ('Left', 99)],
                [('Down', 84), ('Right', 116)],
                [('Down', 85), ('Left', 101)],
                [('Down', 86), ('Left', 102)],
                [('Down', 87), ('Left', 103), ('Right', 119)],
                [('Down', 88), ('Right', 120)],
                [('Down', 89), ('Right', 121)],
                [('Down', 90), ('Left', 106)],
                [('Down', 91), ('Left', 107), ('Right', 123)],
                [('Down', 92), ('Right', 124)],
                [('Down', 93), ('Left', 109), ('Right', 125)],
                [('Down', 94), ('Right', 126)],
                [('Down', 95), ('Right', 127)],
                [(1, 0)],
                [(1, 1)],
                [(1, 2)],
                [(0.1, 160), (0.9, 3)],
                [(1, 4)],
                [(1, 5)],
                [(0.1, 160), (0.9, 6)],
                [(1, 7)],
                [(1, 8)],
                [(1, 9)],
                [(1, 10)],
                [(1, 11)],
                [(1, 12)],
                [(1, 13)],
                [(0.1, 160), (0.9, 14)],
                [(1, 15)],
                [(0.1, 64), (0.9, 68)],
                [(0.1, 65), (0.9, 69)],
                [(0.1, 66), (0.9, 70)],
                [(0.1, 67), (0.9, 71)],
                [(0.1, 68), (0.9, 72)],
                [(0.1, 69), (0.9, 73)],
                [(0.1, 70), (0.9, 74)],
                [(0.1, 71), (0.9, 75)],
                [(0.1, 72), (0.9, 76)],
                [(0.1, 73), (0.9, 77)],
                [(0.1, 74), (0.9, 78)],
                [(0.1, 75), (0.9, 79)],
                [(0.1, 76), (0.9, 161)],
                [(0.1, 77), (0.9, 161)],
                [(0.1, 78), (0.9, 161)],
                [(0.1, 79), (0.9, 161)],
                [(0.1, 64), (0.9, 67)],
                [(0.1, 65), (0.9, 64)],
                [(0.1, 66), (0.9, 65)],
                [(0.1, 67), (0.9, 66)],
                [(0.1, 68), (0.9, 71)],
                [(0.1, 69), (0.9, 68)],
                [(0.1, 70), (0.9, 69)],
                [(0.1, 71), (0.9, 70)],
                [(0.1, 72), (0.9, 75)],
                [(0.1, 73), (0.9, 72)],
                [(0.1, 74), (0.9, 73)],
                [(0.1, 75), (0.9, 74)],
                [(0.1, 76), (0.9, 79)],
                [(0.1, 77), (0.9, 76)],
                [(0.1, 78), (0.9, 77)],
                [(0.1, 79), (0.9, 78)],
                [(0.1, 64), (0.9, 65)],
                [(0.1, 65), (0.9, 66)],
                [(0.1, 66), (0.9, 67)],
                [(0.1, 67), (0.9, 64)],
                [(0.1, 68), (0.9, 69)],
                [(0.1, 69), (0.9, 70)],
                [(0.1, 70), (0.9, 71)],
                [(0.1, 71), (0.9, 68)],
                [(0.1, 72), (0.9, 73)],
                [(0.1, 73), (0.9, 74)],
                [(0.1, 74), (0.9, 75)],
                [(0.1, 75), (0.9, 72)],
                [(0.1, 76), (0.9, 77)],
                [(0.1, 77), (0.9, 78)],
                [(0.1, 78), (0.9, 79)],
                [(0.1, 79), (0.9, 76)],
                [(0.05, 48), (0.95, 16)],
                [(0.05, 49), (0.95, 17)],
                [(0.05, 50), (0.95, 18)],
                [(0.05, 51), (0.95, 19)],
                [(0.05, 52), (0.95, 20)],
                [(0.05, 53), (0.95, 21)],
                [(0.05, 54), (0.95, 22)],
                [(0.05, 55), (0.95, 23)],
                [(0.05, 56), (0.95, 24)],
                [(0.05, 57), (0.95, 25)],
                [(0.05, 58), (0.95, 26)],
                [(0.05, 59), (0.95, 27)],
                [(0.05, 60), (0.95, 28)],
                [(0.05, 61), (0.95, 29)],
                [(0.05, 62), (0.95, 30)],
                [(0.05, 63), (0.95, 31)],
                [(0.05, 48), (0.95, 32)],
                [(0.05, 49), (0.95, 33)],
                [(0.05, 50), (0.95, 34)],
                [(0.05, 51), (0.95, 35)],
                [(0.05, 52), (0.95, 36)],
                [(0.05, 53), (0.95, 37)],
                [(0.05, 54), (0.95, 38)],
                [(0.05, 55), (0.95, 39)],
                [(0.05, 56), (0.95, 40)],
                [(0.05, 57), (0.95, 41)],
                [(0.05, 58), (0.95, 42)],
                [(0.05, 59), (0.95, 43)],
                [(0.05, 60), (0.95, 44)],
                [(0.05, 61), (0.95, 45)],
                [(0.05, 62), (0.95, 46)],
                [(0.05, 63), (0.95, 47)],
                [(1, 160)],
                [(1, 161)]],
            'final_states': [161]}
}
