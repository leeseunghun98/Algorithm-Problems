import sys
input = sys.stdin.readline
n, k = map(int, input().split())
cases = [[[], []] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    cases[a][1].append(b)
    cases[b][0].append(a)

s = int(input())
questions = [tuple(map(int, input().split())) for _ in range(s)]
ways = [[0 for _ in range(n+1)] for _ in range(n+1)]

def up(start, pos):
    for parent in cases[pos][0]:
        if not ways[start][parent]:
            ways[start][parent] = 1
            up(start, parent)

def down(start, pos):
    for child in cases[pos][1]:
        if not ways[start][child]:
            ways[start][child] = -1
            down(start, child)

for i in range(1, n+1):
    if ways[i][i] == 0:
        ways[i][i] = 1
        up(i, i)
        down(i, i)

for start, finish in questions:
    print(ways[start][finish])