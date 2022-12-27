# import psutil
# p = psutil.Process()
# def memory_usage(message: str = 'debug'):
#     # current process RAM usage
#     p = psutil.Process()
#     rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
#     print(f"[{message}] memory usage: {rss: 10.5f} MB")


import sys
import heapq
MAX = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
countries = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    countries[a].append((b, c))
    countries[b].append((a, c))

start, finish = map(int, input().split())

visited = [0 for _ in range(n+1)]
queue = [(-MAX, start)]
visited[1] = 1
while queue:
    th, pos = heapq.heappop(queue)
    visited[pos] = 1
    if pos == finish:
        print(-th)
        break
    for next_pos, next_cost in countries[pos]:
        if visited[next_pos]:
            continue
        heapq.heappush(queue, (max(-next_cost, th), next_pos))