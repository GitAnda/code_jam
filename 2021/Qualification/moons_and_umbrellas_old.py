def min_cost(s, x, y):
    si_prev = None
    n = 0
    cost = 0
    print(f'X={x}, Y={y}, {s}' )

    def sub_cost(prev, curr, n):
        if curr == prev:  # C__C or J__J
            return min(0, (n + 1) // 2 * (x + y))
        elif curr == 'C' and prev == 'J':  # J__C
            return y + min(0, n // 2 * (x + y))
        elif curr == 'J' and prev == 'C':  # C__J
            return x + min(0, n // 2 * (x + y))
        else:
            print(f'Error, unexpected arguments: {prev}, {curr}')

    for si in s:
        if si == '?':
            n += 1
            continue

        if si_prev == None:
            if n != 0:
                cost += min(sub_cost('C', si, n - 1), sub_cost('J', si, n - 1))
        else:
            cost += sub_cost(si_prev, si, n)

        print(f'{si_prev}{"?"*n + si} {cost}')
        si_prev = si
        n = 0

    if si[-1] == '?':
        cost += min(sub_cost(si_prev, 'C', n - 1), sub_cost(si_prev, 'J', n - 1))
        print(f'{si_prev}{"?"*n} {cost}')

    return cost

import sys
with open(sys.argv[0][:-3] + '.txt', 'r') as f:

    T = int(f.readline())
    for t in range(T):
        X, Y, S = f.readline().strip().split(" ")
        print(f'Case #{t + 1}: {min_cost(S, int(X), int(Y))}')