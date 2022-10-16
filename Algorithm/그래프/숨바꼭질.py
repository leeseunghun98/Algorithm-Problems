from collections import deque
n, k = map(int, input().split())
queue = deque([([n], 0)])
visited = [0 for _ in range(200000)]
while queue:
    j = queue.popleft()
    if k in j[0]:
        answer = j[1]
        break
    lst = []
    for i in j[0]:
        if i-1 >= 0 and visited[i-1] == 0:
            lst.append(i-1)
            visited[i-1] = 1
        if i+1 <= k and visited[i+1] == 0:
            lst.append(i+1)
            visited[i+1] = 1
        if 2*i <= 1.5 * k and visited[i*2] == 0:
            lst.append(i*2)
            visited[2*i] = 1
    queue.append((lst, j[1]+1))
print(answer)