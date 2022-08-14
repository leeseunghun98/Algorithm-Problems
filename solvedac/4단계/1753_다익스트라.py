# 다익스트라 알고리즘
import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
li = [[] for _ in range(v+1)]
result = [3000001 for _ in range(v+1)]
for i in range(e):
    s, f, w = map(int, input().split())
    li[s].append((f, w))

queue = []
def solve(start):
    result[start] = 0
    heapq.heappush(queue, [0, start])
    while queue:
        cur_w, cur_pos = heapq.heappop(queue)
        for next_pos, w in li[cur_pos]:
            next_w = cur_w + w
            if next_w < result[next_pos]:
                result[next_pos] = next_w
                heapq.heappush(queue, [next_w, next_pos])
solve(k)
for i in result[1:]:
    if i == 3000001:
        print('INF')
    else:
        print(i)



# # bfs풀이
# import sys
# from collections import deque
# input = sys.stdin.readline
# v, e = map(int, input().split())
# k = int(input())
# li = [[] for _ in range(v+1)]
# result = [3000001 for _ in range(v+1)]
# for i in range(e):
#     s, f, w = map(int, input().split())
#     li[s].append((f, w))

# def solve(start):
#     result[start] = 0
#     queue = deque()
#     queue.append(start)
#     while queue:
#         j = queue.popleft()
#         for i in li[j]:
#             if result[j] + i[1] < result[i[0]]:
#                 result[i[0]] = result[j] + i[1]
#                 queue.append(i[0])
# solve(k)
# for i in result[1:]:
#     if i == 3000001:
#         print('INF')
#     else:
#         print(i)
