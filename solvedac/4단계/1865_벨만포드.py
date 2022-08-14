import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
def solve(start, li):
    queue = []
    result = [INF for _ in range(len(li))]
    heapq.heappush(queue, [0, start])
    while queue:
        cur_w, cur_pos = heapq.heappop(queue)
        for dest, w in li[cur_pos]:
            next_w = cur_w + w
            if next_w < 0 and dest == start:
                result[dest] = next_w
                heapq.heappush(queue, [next_w, dest])
                return 'YES'
            elif next_w < result[dest]:
                result[dest] = next_w
                heapq.heappush(queue, [next_w, dest])
    return 'NO'

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    warms = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])
        warms.append(e)
    for i in warms:
        print(solve(1, graph))