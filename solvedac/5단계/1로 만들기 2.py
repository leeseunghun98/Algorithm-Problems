from collections import deque
n = int(input())
visited = [0 for _ in range(n+1)]
queue = deque([n])
visited[n] = n
li = []
while queue:
    j = queue.popleft()
    if j == 1:
        break
    if j % 3 == 0 and visited[j//3] == 0:
        queue.append(j//3)
        visited[j//3] = j
    if j % 2 == 0 and visited[j//2] == 0:
        queue.append(j//2)
        visited[j//2] = j
    if visited[j-1] == 0 and j-1 > 0:
        queue.append(j-1)
        visited[j-1] = j
num = 1
while num != n:
    li.append(num)
    num = visited[num]
li.append(n)
print(len(li)-1)
print(*reversed(li))