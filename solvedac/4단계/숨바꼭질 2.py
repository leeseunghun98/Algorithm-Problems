from collections import deque
n, k = map(int, input().split())

queue = deque([n])
answer = 0
visited = [int(1e6) for _ in range(100001)]
visited[n] = 0
while queue:
    j = queue.popleft()
    if j == k:
        answer += 1
        continue
    
    for i in [j*2, j+1, j-1]:
        if 0 <= i < 100001 and visited[i] >= visited[j] + 1:
            queue.append(i)
            visited[i] = visited[j]+1

print(visited[k])
print(answer)