def rock_paper_scissors(p1, p2):
    if (p1 == 'R' and p2 == 'T') or (p1 == 'P'
                                     and p2 == 'R') or (p1 == 'T'
                                                        and p2 == 'P'):
        return 1
    elif (p2 == 'R' and p1 == 'T') or (p2 == 'P'
                                       and p1 == 'R') or (p2 == 'T'
                                                          and p1 == 'P'):
        return 2
    else:
        return 0


def play(op1, op2):
    wins = {}
    for i in range(len(op1)):
        winner = rock_paper_scissors(op1[i], op2[i])
        if winner != 0:
            wins[winner] = wins.get(winner, 0) + 1
    return wins


player1 = list(input())
player2 = list(input())
result = play(player1, player2)
for key, value in result.items():
    print(key, value)
