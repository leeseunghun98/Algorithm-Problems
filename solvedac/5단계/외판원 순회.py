# 성공
import sys
N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * (1 << N - 1) for _ in range(N)]

def solution(i, route):
    if dp[i][route] != 0:
        return dp[i][route]

    if route == (1 << (N - 1)) - 1:
        if W[i][0]:
            return W[i][0]
        else:
            return float('inf')
            
    min_dist = float('inf')
    for j in range(1, N):
        if not W[i][j]:
            continue
        if route & (1 << j - 1):
            continue
        dist = W[i][j] + solution(j, route | (1 << (j - 1)))
        if min_dist > dist:
            min_dist = dist
    dp[i][route] = min_dist
    
    return min_dist

print(solution(0, 0))


## 시간초과
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
dp = [[INF] * (1 << n) for _ in range(n)]

# start, visited로 index접근
def dfs(start, visited):
    if visited == (1 << n) - 1:
        if dp[start][visited] != INF:
            return dp[start][visited]
        if li[start][0] == 0:
            return INF
        return li[start][0]

    
    for i in range(1, n):
        if (li[start][i] != 0) and (not (visited & (1 << i))):
            dp[start][visited] = min(dp[start][visited], dfs(i, visited | (1 << i)) + li[start][i])

    return dp[start][visited]

print(dfs(0, 1))




## 시간 초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# li = [tuple(map(int, input().split())) for _ in range(n)]

# visited = [0 for _ in range(n)]

# def dfs(start, dist , depth):
#     if start == 0 and depth == n:
#         return dist
#     if start == 0 and depth > 0:
#         return float("INF")
#     ans = float("INF")
#     for next, cost in enumerate(li[start]):
#         if visited[next] == 0:
#             visited[next] = 1
#             ans = min(dfs(next, dist + cost, depth + 1), ans)
#             visited[next] = 0
#     return ans

# print(dfs(0, 0, 0))

