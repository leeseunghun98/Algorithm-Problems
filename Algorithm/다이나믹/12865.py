import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split())
li = [list(map(int, input().strip().split())) for _ in range(N)]
result = [[0, 0] for _ in range(K+1)]

for i in range(1, K+1):
    max_li = []
    for j in range(1, i):
        max_ = 0
        for k in result[j][1]: # 안갔던 곳
            if j + li[k][0] <= K: # 안갔던 곳중 하나하나 되는지 확인
                max_ = max(max_, result[j][0] + li[k][1])
        max_li.append(max_)
    max_ = 0
    for j in li:
        if j[0] <= K:
            max_ = max(max_, j[1])
    result[i][0] = max(max_li)
    result[i][1] = 