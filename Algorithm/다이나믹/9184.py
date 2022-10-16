import sys
dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
while True:
    a = list(map(int, sys.stdin.readline().strip().split()))
    if a == [-1, -1, -1]:
        break
    print('w({}, {}, {}) ='.format(a[0], a[1], a[2]), end=' ')
    if a[0] < 1 or a[1] < 1 or a[2] < 1:
        print(1)
        continue
    elif a[0] > 20 or a[1] > 20 or a[2] > 20:
        print(dp[20][20][20])
        continue
    print(dp[a[0]][a[1]][a[2]])