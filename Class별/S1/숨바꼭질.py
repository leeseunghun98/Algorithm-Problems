import sys
input = sys.stdin.readline
n, m = map(int, input().split())
roads = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

stack = [1]
ret = 0
visited = [0 for _ in range(n+1)]
visited[1] = 1
while stack:
    nexts = []
    cnt = len(stack)
    first = stack[0]
    while stack:
        pos = stack.pop()
        if pos < first:
            first = pos
        for next in roads[pos]:
            if not visited[next]:
                nexts.append(next)
                visited[next] = 1
    stack = nexts
    ret += 1
print(first, ret-1, cnt)