cache = {}

def check_cache(y):
    nry = float('inf')
    for ry in cache.keys():
        if ry >= y:
            nry = min(nry, ry)

    if nry == float('inf'): return False, None

    prev_y = cache[nry]
    if y < prev_y:
        return False, None
    else:
        return True, nry

def next_roaring_year(y):
    in_cache, ry = check_cache(y)
    if in_cache:
        return ry



    next_roaring_year = 0
    cache[y] = next_roaring_year
    return next_roaring_year

import sys
with open(sys.argv[0][:-3] + '.txt', 'r') as f:

    T = int(f.readline())
    for t in range(T):
        Y = int(f.readline())
        print(f'Case #{t + 1}: {next_roaring_year(Y)}')
