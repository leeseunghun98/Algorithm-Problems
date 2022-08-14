import sys
import heapq
INF = float("inf")
input = sys.stdin.readline
n = int(input())
m = int(input())
li = [[] for _ in range(n+1)]
for _ in range(m):
    s, f, v = map(int, input().split())
    li[s].append([v, f])
s, f = map(int, input().split())

def dijkstra(s, f):
    visited = [INF] * (n+1)
    queue = []
    heapq.heappush(queue, [0, s])
    while queue:
        cur_val, cur_pos = heapq.heappop(queue)
        if cur_pos == f:
            print(cur_val)
            return
        for next_val, next_pos in li[cur_pos]:
            if visited[next_pos] > cur_val + next_val:
                visited[next_pos] = cur_val + next_val
                heapq.heappush(queue, [cur_val + next_val, next_pos])
                
dijkstra(s, f)