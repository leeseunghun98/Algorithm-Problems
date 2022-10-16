from collections import deque

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
answer = -1
ans = 0
queue = deque()
queue.append((0, 0))
visited = [0 for _ in range(k+1)]
while queue:
    cnt, pos = queue.popleft()
    for coin in coins:
        now = coin + pos
        if now > k:
            continue
        elif now == k:
            ans = 1
            answer = cnt + 1
            break
        elif visited[now] == 0:
            visited[now] = 1
            queue.append((cnt+1, now))
    if ans == 1:
        break
print(answer)