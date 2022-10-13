import sys
from collections import deque
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    seq = [[0, []] for _ in range(n+1)] # ->, <-
    for _ in range(k):
        s, e = map(int, input().split())
        seq[s][1].append(e)
        seq[e][0] += 1
    w = int(input())
    starts = []
    for i in range(1, n+1):
        if seq[i][0] == 0:
            starts.append(i)
    queue = deque(starts)
    visited = [0 for _ in range(n+1)]
    for start in starts:
        visited[start] = times[start]
    while queue:
        pos = queue.popleft()
        for n in seq[pos][1]:
            seq[n][0] -= 1
            if seq[n][0] == 0:
                queue.append(n)
            visited[n] = max(visited[n], visited[pos] + times[n])
    print(visited[w])