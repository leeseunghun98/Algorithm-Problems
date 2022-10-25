import sys
import math
input = sys.stdin.readline
testcase = int(input())
INF = float("inf")

def dfs(idx, x, y, pluses):
    if idx == n:
        if pluses == n//2:
            ret = math.sqrt(x**2 + y**2)
            if answer[0] > ret:
                answer[0] = ret
        return
    if pluses < n//2:
        dfs(idx+1, x+li[idx][0], y+li[idx][1], pluses+1)
    if idx - pluses < n//2:
        dfs(idx+1, x-li[idx][0], y-li[idx][1], pluses)

for _ in range(testcase):
    n = int(input())
    li = [tuple(map(int, input().split())) for _ in range(n)]
    answer = [INF]
    dfs(0, 0, 0, 0)
    print(answer[0])