from itertools import combinations_with_replacement
n, m = map(int, input().split())
li = [i+1 for i in range(n)]
for i in combinations_with_replacement(li, m):
    print(*i)