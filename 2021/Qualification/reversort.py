def reversort(L):
    cost = 0

    for i in range(len(L)-1):
        subL = L[i:]
        j = subL.index(min(subL)) + i
        L = L[:i] + list(reversed(L[i:j+1])) + L[j+1:]
        cost += j - i + 1
        # print(i, j, cost)

    return cost

import sys
with open(sys.argv[0][:-3] + '.txt', 'r') as f:

    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        L = [int(l) for l in f.readline().strip().split(" ")]
        print(f'Case #{t + 1}: {reversort(L)}')