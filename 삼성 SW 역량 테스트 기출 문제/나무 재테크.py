import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
li = [[[5, deque([])] for _ in range(n)] for _ in range(n)]
A = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

for tree in trees:
    li[tree[0]-1][tree[1]-1][1].append((tree[2], 1))

for _ in range(k):
    for x in range(n):
        for y in range(n):
            #봄
            forsummer = 0
            for _ in range(len(li[x][y][1])):
                a, b = li[x][y][1].popleft()
                if a * b <= li[x][y][0]:
                    li[x][y][0] -= a * b
                    li[x][y][1].append((a+1, b))
                else:
                    cnt = li[x][y][0] // a
                    if cnt:
                        li[x][y][0] -= a * cnt
                        forsummer += (b - cnt) * (a // 2)
                        li[x][y][1].append((a+1, cnt))
                    else:
                        forsummer += b * (a // 2)
            #여름
            li[x][y][0] += forsummer
    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):    
            #가을
            spread = 0
            for i in li[x][y][1]:
                if i[0] % 5 == 0:
                    spread += i[1]
            for i in range(8):
                nx = dx[i] + x
                ny = dy[i] + y
                if (0<=nx<n) and (0<=ny<n):
                    visited[nx][ny] += spread
            
            #겨울
            li[x][y][0] += A[x][y]
    for x in range(n):
        for y in range(n):
            if visited[x][y] > 0:
                li[x][y][1].appendleft((1, visited[x][y]))

answer = 0
for x in range(n):
    for y in range(n):
        for i in li[x][y][1]:
            answer += i[1]
print(answer)






















# import sys
# n, m, k = map(int, sys.stdin.readline().split())
# li = [[[5, []] for _ in range(n)] for _ in range(n)]
# A = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# trees = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
# dx = (-1, -1, -1, 0, 0, 1, 1, 1)
# dy = (-1, 0, 1, -1, 1, -1, 0, 1)

# for x, y, age in trees:
#     li[x-1][y-1][1].append([age, 1])
    
# for _ in range(k):
    
    
#     for x in range(n):
#         for y in range(n):
#             # 봄
#             lst = li[x][y][1]
#             yang = 0
#             for i in range(len(lst)):
#                 if li[x][y][0] - lst[i][0] * lst[i][1] >= 0:
#                     li[x][y][0] -= (lst[i][0] * lst[i][1])
#                     lst[i][0] += 1
#                 else:
#                     cnt = li[x][y][0] // lst[i][0]
#                     yang += (lst[i][1] - cnt) * (lst[i][0] // 2)
#                     for j in range(i+1, len(lst)):
#                         if lst[j][1] > 0:
#                             yang += lst[j][1] * (lst[j][0] // 2)
#                     if cnt:
#                         lst[i][0] += 1
#                         lst[i][1] = cnt
#                         lst = lst[:i+1]
#                     else:
#                         li[x][y][1] = lst[:i]
#                     break
#             # 여름
#             li[x][y][0] += yang
    
#     visited = [[0 for _ in range(n)] for _ in range(n)]
#     for x in range(n):
#         for y in range(n):
#             lst = li[x][y][1]
#             # 가을
#             re = 0
#             for l in lst:
#                 if l[0] % 5 == 0:
#                     re += l[1]
#             for j in range(8):
#                 nx = x + dx[j]
#                 ny = y + dy[j]
#                 if (0<=nx<n) and (0<=ny<n):
#                     visited[nx][ny] += re
            
#             # 겨울
#             li[x][y][0] += A[x][y]
    
#     for x in range(n):
#         for y in range(n):
#             if visited[x][y] > 0:
#                 li[x][y][1] = [[1, visited[x][y]]] + li[x][y][1]

# answer = 0
# for i in li:
#     for j in i:
#         for a in range(len(j[1])):
#             answer += j[1][a][1]
# print(answer)






# import sys
# n, m, k = map(int, sys.stdin.readline().split())
# li = [[[5, [0 for _ in range(200)]] for _ in range(n)] for _ in range(n)]
# A = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
# trees = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
# dx = (-1, -1, -1, 0, 0, 1, 1, 1)
# dy = (-1, 0, 1, -1, 1, -1, 0, 1)
# for x, y, age in trees:
#     li[x-1][y-1][1][age] += 1

# for _ in range(k):
    
#     for x in range(n):
#         for y in range(n):
#             # 봄
#             lst = li[x][y][1]
#             tmp = 0
#             temp = 0
#             yang = 0
#             for i in range(200):
#                 if li[x][y][0] - i * lst[i] >= 0:
#                     temp = tmp
#                     li[x][y][0] -= i * lst[i]
#                     tmp = lst[i]
#                     lst[i] = temp
#                     temp = 0
#                 else:
#                     cnt = li[x][y][0] // i
#                     yang += (lst[i] - cnt) * (i // 2)
#                     yang += lst[i+1] * ((i+1) // 2)
#                     lst[i] = tmp
#                     lst[i+1] = cnt
#                     for j in range(i+2, 200):
#                         if lst[j] > 0:
#                             yang += lst[j] * (i // 2)
#                             lst[j] = 0
#                     break
#             # 여름
#             li[x][y][0] += yang
            
#     for x in range(n):
#         for y in range(n):
#             lst = li[x][y][1]
#             # 가을
#             re = 0
#             for i in range(5, 196, 5):
#                 re += lst[i]
#             for j in range(8):
#                 nx = x + dx[j]
#                 ny = y + dy[j]
#                 if (0<=nx<n) and (0<=ny<n):
#                     li[nx][ny][1][1] += re
            
#             # 겨울
#             li[x][y][0] += A[x][y]

# answer = 0
# for i in li:
#     for j in i:
#         for a in range(200):
#             answer += j[1][a]
# print(answer)
