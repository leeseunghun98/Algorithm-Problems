import sys
input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()

dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

mx = dp[-1][-1]
print(mx)
answer = []
if mx != 0:
    for i in range(len(s1), 0, -1):
        if dp[-1][i] == mx and dp[-1][i-1] != mx:
            answer.append(s1[i-1])
            mx -= 1
    print(*reversed(answer), sep="")