li = [0, 5, 1, 2, 3, 4, 9, 6, 7, 8]
n = len(li)-1

ans = []
visited = [0 for _ in range(n+1)]
for start in range(1, n+1):
    if not visited[start]:
        visited[start] = 1
        next = li[start]
        if next == start:
            continue
        length = 1
        while next != start:
            visited[next] = 1
            length += 1
            next = li[next]
        ans.append(length)
answer = 0
print(ans)
for i in ans:
    answer += i*(i-1)//2
print(answer)