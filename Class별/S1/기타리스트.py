import sys
from collections import deque
input = sys.stdin.readline
n, start, m = map(int, input().split())
volumes = tuple(map(int, input().split()))
visited = [[0 for _ in range(m+1)] for _ in range(n)]

starts = deque([])
if start - volumes[0] >= 0:
    starts.append((0, start-volumes[0]))
    visited[0][start-volumes[0]]
if start + volumes[0] <= m:
    starts.append((0, start+volumes[0]))
    visited[0][start+volumes[0]]
answer = -1
while starts:
    idx, amt = starts.popleft()
    if idx == n-1:
        answer = max(answer, amt)
        continue
    if amt - volumes[idx+1] >= 0 and not visited[idx+1][amt-volumes[idx+1]]:
        starts.append((idx+1, amt-volumes[idx+1]))
        visited[idx+1][amt-volumes[idx+1]] = 1
    if amt + volumes[idx+1] <= m and not visited[idx+1][amt+volumes[idx+1]]:
        starts.append((idx+1, amt+volumes[idx+1]))
        visited[idx+1][amt+volumes[idx+1]] = 1
print(answer)
