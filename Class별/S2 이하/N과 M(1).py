from itertools import permutations
n, m = map(int, input().rsplit())
for per in permutations(tuple(i for i in range(1, n+1)), m):
    print(*per)