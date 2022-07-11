def max_win_chance(p, k):
    p = [0] + p + [k + 1]
    wins = {}
    for i in range(len(p) - 1):
        d = p[i + 1] - p[i] - 1

        if d == 1:
            wins[p[i] + 1] = d

        elif d > 1:
            if p[i] == 0:
                wins[p[i + 1] - 1] = d
            elif p[i + 1] == k + 1:
                wins[p[i] + 1] = d
            else:
                wins[p[i] + 1] = d // 2
                wins[p[i + 1] - 1] = - (-d // 2)

    print(wins)

    total_wins = 0
    for _ in range(2):
        if not wins: return total_wins / k
        best_number = max(wins, key=lambda x: wins[x])
        total_wins += wins[best_number]
        wins.pop(best_number)

    return total_wins / k

import sys
file = sys.argv[0][:-3] + '.txt'
with open(file, 'r') as f:

    T = int(f.readline())
    for t in range(T):
        N, K = [int(s) for s in f.readline().strip().split(" ")]
        P = sorted(set([int(s) for s in f.readline().strip().split(" ")]))
        print(f'Case #{t + 1}: {max_win_chance(P, K)}')
