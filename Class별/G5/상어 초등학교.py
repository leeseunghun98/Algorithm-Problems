import sys
input = sys.stdin.readline
n = int(input())
students = [[] for _ in range(n**2 + 1)]
orders = []
boundary = lambda x, y : True if (0<=x<n) and (0<=y<n) else False
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for _ in range(n**2):
    a = list(map(int, input().split()))
    students[a[0]] = a[1:]
    orders.append(a[0])

empty = [[i, j] for i in range(n) for j in range(n)]
room = [[0 for _ in range(n)] for _ in range(n)]
score = [0, 1, 10, 100, 1000]

for student in orders:
    likes = students[student]
    seat = empty[0]
    seat_count = 0
    seat_blank = 0
    for x in range(n):
        for y in range(n):
            if room[x][y] != 0:
                continue
            count = 0
            blank = 0
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if boundary(nx, ny):
                    if room[nx][ny] in likes:
                        count += 1
                    elif room[nx][ny] == 0:
                        blank += 1
            if count > seat_count:
                seat_count = count
                seat = [x, y]
                seat_blank = blank
            elif count == seat_count:
                if blank > seat_blank:
                    seat_count = count
                    seat = [x, y]
                    seat_blank = blank
                elif blank == seat_blank:
                    if seat[0] > x or (seat[0] == x and seat[1] > y):
                        seat_count = count
                        seat = [x, y]
                        seat_blank = blank
    room[seat[0]][seat[1]] = student
    empty.remove(seat)

answer = 0
for x in range(n):
    for y in range(n):
        ans = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if boundary(nx, ny) and room[nx][ny] in students[room[x][y]]:
                ans += 1
        answer += score[ans] 
print(answer)