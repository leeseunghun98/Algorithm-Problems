def rotate_right(lst):
    lst = [lst[-1]] + lst[:-1]
    return lst
def rotate_left(lst):
    lst = lst[1:] + [lst[0]]
    return lst
wheels = [[0] * 8] + [list(input()) for _ in range(4)] + [[0] * 8]
k = int(input())
rolls = [list(map(int, input().split())) for _ in range(k)]

def roll(wheels, spin, now, before):
    left, right = 0, 0
    if (now >= 1) and wheels[now][6] != wheels[now-1][2]:
        left = 1
    if (now < 5) and wheels[now][2] != wheels[now+1][6]:
        right = 1
    if before == now:
        if left == 1:
            roll(wheels, -spin, now-1, now)
        if right == 1:
            roll(wheels, -spin, now+1, now)
    elif before > now:
        if left == 1:
            roll(wheels, -spin, now-1, now)
    else:
        if right == 1:
            roll(wheels, -spin, now+1, now)
    if spin == -1:
        wheels[now] = rotate_left(wheels[now])
    else:
        wheels[now] = rotate_right(wheels[now])
        
for i in rolls:
    roll(wheels, i[1], i[0], i[0])

answer = 0
for idx, i in enumerate(wheels[1:5]):
    answer += ((2 ** (idx)) * int(i[0]))
print(answer)