import sys
N, M = map(int, sys.stdin.readline().strip().split())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
plus = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
dp = [[[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        for a in range(i, N+1):
            for b in range(j, N+1):
                e = 0
                for q in range(i, a+1):
                    for w in range(j, b+1):
                        e += li[q-1][w-1]
                dp[i][j][a][b] = e
for i in plus:
    print(dp[i[0]][i[1]][i[2]][i[3]])