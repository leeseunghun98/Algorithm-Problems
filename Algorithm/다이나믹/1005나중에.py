import sys
input = sys.stdin.readline
testcase = int(input().strip())
def find(start):
    for i in graph[start]:
        a = dp[i]
        if dp[start] < a:
            dp[start] = a
    if dp[start] == 0:
        return times[start - 1]
    else:
        return dp[start] + times[start - 1]
for _ in range(testcase):
    n, lines = map(int, input().strip().split())
    times = list(map(int, input().strip().split()))
    li = [0] + [list(map(int, input().strip().split())) for _ in range(lines)]
    want = int(input().strip())
    graph = [[] for _ in range(n+1)]
    dp = [0] * (n+1)
    for i in li[1:]:
        graph[i[1]].append(i[0])
    print(find(want))
    print(dp)
    
    
# import sys
# input = sys.stdin.readline
# testcase = int(input().strip())
# def find(start):
#     mx = 0
#     for i in graph[start]:
#         a = find(i)
#         if mx < a:
#             mx = a
#     if mx == 0:
#         return times[start - 1]
#     else:
#         return mx + times[start - 1]
# for _ in range(testcase):
#     n, lines = map(int, input().strip().split())
#     times = list(map(int, input().strip().split()))
#     li = [0] + [list(map(int, input().strip().split())) for _ in range(lines)]
#     want = int(input().strip())
#     graph = [[] for _ in range(n+1)]
#     dp = [0] * (n+1)
#     for i in li[1:]:
#         graph[i[1]].append(i[0])
#     print(find(want))