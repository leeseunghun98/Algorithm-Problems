N = int(input())
dragons = [tuple(map(int, input().split())) for _ in range(N)]

dragon_generation = [[(1, 0)]]

def turn(drgon_gen):
    lines = []
    for line in drgon_gen:
        lines.append((line[1], -line[0]))
    return lines

for _ in range(10):
    dragon_generation.append(dragon_generation[-1] + turn(dragon_generation[-1][::-1]))

answer = 0

def chk(visited, x, y):
    re = 0
    if visited[y][x-1] == 1:
        if visited[y-1][x-1] == 1 and visited[y-1][x] == 1:
            re += 1
        if visited[y+1][x-1] == 1 and visited[y+1][x] == 1:
            re += 1
    if visited[y][x+1] == 1:
        if visited[y-1][x+1] == 1 and visited[y-1][x] == 1:
            re += 1
        if visited[y+1][x+1] == 1 and visited[y+1][x] == 1:
            re += 1
    return re

visited = [[0 for _ in range(103)] for _ in range(103)]
for dragon in dragons:
    each_dragon = dragon_generation[dragon[3]]
    for _ in range(dragon[2]):
        each_dragon = turn(each_dragon)
    x = dragon[0] + 1
    y = dragon[1] + 1
    if visited[y][x] == 0:
        answer += chk(visited, x, y)
        
    visited[y][x] = 1
    for i in each_dragon:
        x += i[0]
        y += i[1]
        if visited[y][x] == 0:
            answer += chk(visited, x, y)
        visited[y][x] = 1

print(answer)