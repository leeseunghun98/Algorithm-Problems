r, c, k = map(int, input().split())
r -= 1
c -= 1

li = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    t, v, u = map(int,input().split())
    li[i][0] = t
    li[i][1] = v
    li[i][2] = u
    
def R(lst):
    longist = 0
    for index, i in enumerate(lst):
        a = [0] * 100
        for j in i:
            if j > 0:
                a[j - 1] += 1
        b = []
        for idx, j in enumerate(a):
            if j > 0:
                b.append((idx + 1, j))
        if len(b) * 2 > longist:
            longist = len(b) * 2
        b.sort(key= lambda x : (x[1], x[0]))
        c = [0] * 100
        for idx, i in enumerate(b):
            if idx >= 50:
                break
            c[2 * idx] = i[0]
            c[2 * idx + 1] = i[1]
        lst[index] = c
    return [lst, longist]
        

def C(lst):
    longist = 0
    for i in range(100):
        a = [0] * 100
        for j in range(100):
            if lst[j][i] > 0:
                a[lst[j][i] - 1] += 1
        b = []
        for idx, j in enumerate(a):
            if j > 0:
                b.append((idx + 1, j))
        if len(b) * 2 > longist:
            longist = len(b) * 2
        b.sort(key= lambda x : (x[1], x[0]))
        for j in range(100):
            lst[j][i] = 0
        for idx, j in enumerate(b):
            if idx >= 50:
                break
            lst[2 * idx][i] = j[0]
            lst[2 * idx + 1][i] = j[1]

    return [lst, longist]

time = 0
r_length = 3
l_length = 3
while li[r][c] != k:
    time += 1
    if time > 100:
        time = -1
        break
    if l_length < r_length:
        li, l_length = C(li)
    else:
        li, r_length = R(li)
    
print(time)
