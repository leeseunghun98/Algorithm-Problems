# import sys
# R, C = map(int, sys.stdin.readline().rstrip('\n').split())
# li = []
# for _ in range(R):
#     li.append(list(sys.stdin.readline().strip('\n')))
# dis = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# did = []
# def dfs(start, graph, visited):
#     visited.append(graph[start[0]][start[1]])
#     for di in dis:
#         if start[0]+di[0]<0 or start[0]+di[0]>=R or start[1]+di[1]<0 or start[1]+di[1]>=C:
#             continue
#         elif graph[start[0]+di[0]][start[1]+di[1]] not in visited:
#             dfs([start[0]+di[0], start[1]+di[1]], graph, visited)
#             did.remove(graph[start[0]+di[0]][start[1]+di[1]])
#     did.append(visited)
            
# dfs([0, 0], li, [])
# mx = 0
# for i in did:
#     mx = max(len(i), mx)
# print(did)

# import sys 
# from collections import deque
# input=sys.stdin.readline
# R,C = map(int, input().split())
# arr=[list(input()) for _ in range(R)]
# check=[0]*(26)

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]
# maxi=0

# def dfs(x,y,cnt):
#     global maxi
#     cnt += 1
#     maxi=max(cnt,maxi)
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if nx<R and ny<C and nx>=0 and ny>=0 and check[ord(arr[nx][ny])-65]==0:
#             check[ord(arr[nx][ny])-65]=1
#             dfs(nx,ny,cnt)
#             check[ord(arr[nx][ny])-65]=0

# check[ord(arr[0][0])-65]=1
# dfs(0,0,0)

# print(maxi)

# pypy3로만 되는 dfs
# import sys
# input = sys.stdin.readline
# R, C = map(int, input().split())
# li = [list(input()) for _ in range(R)]

# dx=[1,-1,0,0]
# dy=[0,0,1,-1]
# chk = [0] * 26
# result = 0
# def dfs(x, y, cnt):
#     global result
#     cnt += 1
#     result = max(cnt, result)
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if (R>nx>=0) and (C>ny>=0) and chk[ord(li[nx][ny])-65] == 0:
#             chk[ord(li[nx][ny])-65] = 1
#             dfs(nx, ny, cnt)
#             chk[ord(li[nx][ny])-65] = 0
# chk[ord(li[0][0])-65] = 1
# dfs(0, 0, 0)
# print(result)


# # 시간초과 BFS
# import sys 
# from collections import deque
# input=sys.stdin.readline
# R,C = map(int, input().split())
# arr=[list(input()) for _ in range(R)]   # 알파벳 arr받고
# dx=[1,-1,0,0] #방향전환
# dy=[0,0,1,-1]
# answer=1
# def bfs(x,y):
#     global answer
#     queue=deque()
#     queue.append([x,y,arr[x][y]])    #시작점, 
#     while queue:
#         x,y,ans=queue.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx>=0 and ny>=0 and nx<R and ny<C and arr[nx][ny] not in ans:  ## not in ans 이 문법에서 속도 deque >> set 임.. set O(1) deque O(n) 
#                 queue.append([nx,ny,ans+arr[nx][ny]])
#                 answer=max(answer,len(ans)+1)

# bfs(0,0)
# print(answer)

# import sys
# from collections import deque
# input = sys.stdin.readline
# R, C = map(int, input().split())
# li = [list(input().strip()) for _ in range(R)]
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs(x, y):
#     global answer
#     queue=deque()
#     queue.append([x, y, li[x][y]])
#     while queue:
#         x, y, ans = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (0<=nx<R) and (0<=ny<C) and li[nx][ny] not in ans:
#                 queue.append([nx, ny, ans+li[nx][ny]])
#                 answer = max(answer, len(ans)+1)
# answer = 1
# bfs(0, 0)
# print(answer)

# ### BFS set -> dx, dy의 순서대로 갈 필요 없는경우 -> 어쩌다보면 dfs가 될 수도 있는 경우 bfs식으로 만들었지만
# import sys

# R, C = map(int, sys.stdin.readline().split())
# board = [list(sys.stdin.readline().strip()) for _ in range(R)]
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# answer = 1
# def BFS(x, y):
#     global answer
#     q = set([(x, y, board[x][y])])
#     while q:
#         x, y, ans = q.pop()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
#                 q.add((nx,ny,ans + board[nx][ny]))
#                 answer = max(answer, len(ans)+1)

# BFS(0, 0)
# print(answer)







