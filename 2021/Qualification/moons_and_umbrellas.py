import sys
sys.setrecursionlimit(10000)


def min_cost(string, x, y):
    def reduce(s):
        if len(s) <= 1:
            return 0

        if s[0] == '?':
            return min(reduce('C' + s[1:]), reduce('J' + s[1:]))

        if s[1] == '?':
            return min(reduce(s[0] + 'C' + s[2:]), reduce(s[0] + 'J' + s[2:]))

        if s[0] == s[1]:
            return reduce(s[1:])

        if s[0] == 'C' and s[1] == 'J':
            return x + reduce(s[1:])

        if s[0] == 'J' and s[1] == 'C':
            return y + reduce(s[1:])

        print('Case not caught!', s)
        return 0

    if x >= 0 and y >= 0:
        si_prev = None
        cost = 0

        for si in string:
            if si == '?':
                continue

            if si_prev != si:
                if si == 'C' and si_prev == 'J':  # JC
                    cost += y
                elif si == 'J' and si_prev == 'C':  # CJ
                    cost += x
                si_prev = si

        return cost

    return reduce(string)


import sys
with open(sys.argv[0][:-3] + '.txt', 'r') as f:

    T = int(f.readline())
    for t in range(T):
        X, Y, S = f.readline().strip().split(" ")
        print(f'Case #{t + 1}: {min_cost(S, int(X), int(Y))}')