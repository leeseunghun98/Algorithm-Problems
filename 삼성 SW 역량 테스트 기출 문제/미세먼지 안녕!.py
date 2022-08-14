import sys

R, C, T = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
air = []
answer = 2
for idx, i in enumerate(li):
    answer += sum(i)
    if i[0] == -1:
        air.append(idx)
up = air[0]
down = air[1]

def spread(lst):
    plus_lst = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if lst[i][j] > 0:
                n = lst[i][j] // 5
                nx = i-1
                ny = j
                if (0 <= nx < R) and (0 <= ny < C) and lst[nx][ny] > -1:
                    plus_lst[nx][ny] += n
                    lst[i][j] -= n
                nx = i+1
                ny = j
                if (0 <= nx < R) and (0 <= ny < C) and lst[nx][ny] > -1:
                    plus_lst[nx][ny] += n
                    lst[i][j] -= n
                nx = i
                ny = j+1
                if (0 <= nx < R) and (0 <= ny < C) and lst[nx][ny] > -1:
                    plus_lst[nx][ny] += n
                    lst[i][j] -= n
                nx = i
                ny = j-1
                if (0 <= nx < R) and (0 <= ny < C) and lst[nx][ny] > -1:
                    plus_lst[nx][ny] += n
                    lst[i][j] -= n
    for i in range(R):
        for j in range(C):
            lst[i][j] += plus_lst[i][j]

def airpass(lst):
    global up
    global down
    global answer
    answer -= (lst[up-1][0] + lst[down+1][0])
    for i in range(down+1, R):
        lst[i-1][0] = lst[i][0]
    for i in range(up-1, -1, -1):
        lst[i+1][0] = lst[i][0]
    lst[0] = lst[0][1:] + [lst[1][-1]]
    lst[-1] = lst[-1][1:] + [lst[-2][-1]]
    for i in range(R-2, down-1, -1):
        lst[i+1][-1] = lst[i][-1]
    for i in range(1, down):
        lst[i-1][-1] = lst[i][-1]
    lst[up][0] = 0
    lst[down][0] = 0
    lst[up] = [-1] + lst[up][:-1]
    lst[down] = [-1] + lst[down][:-1]
    

for _ in range(T):
    spread(li)
    airpass(li)
print(answer)