import sys
input = sys.stdin.readline
n = int(input())
li = [0] + list(map(int, input().split()))
m = int(input())
table = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    table[i][i] = 1
for i in range(n-1, 0, -1):
    for j in range(2, n+1):
        if j <= i:
            continue
        elif j - i == 1:
            if li[j] == li[i]:
                table[i][j] = 1
        else:
            if table[i+1][j-1] and li[i] == li[j]:
                table[i][j] = 1

for _ in range(m):
    a, b = map(int, input().split())
    print(table[a][b])