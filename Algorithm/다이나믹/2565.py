import sys
input = sys.stdin.readline
n = int(input().strip())
li = [list(map(int, input().strip().split())) for _ in range(n)]
dp = [1]
mx = 1
result = 0
while True:
    len_ = len(li)
    dp = [0] * len_
    for i in range(len_):
        cnt = 0
        for j in range(len_):
            if j == i:
                continue
            elif li[i][0] > li[j][0] and li[i][1] < li[j][1]:
                cnt += 1
            elif li[i][0] < li[j][0] and li[i][1] > li[j][1]:
                cnt += 1
        dp[i] = cnt
    idx = 0
    mx = 0
    for i in range(len_):
        if dp[i] > mx:
            mx = dp[i]
            idx = i
    if mx == 0:
        break
    li.pop(idx)
    result += 1
print(result)
