a, b, c, d = map(int, input().split())

def get_num(x, y):
    mx = (max(abs(x), abs(y)))
    if mx == 0:
        return 1
    if x == mx and y == mx:
        return (2*(mx+1)-1)**2
    byun = 2*mx+1
    start = (byun-2)**2
    if y == mx:
        return start + mx - x
    elif x == -mx:
        return start + byun - 1 + mx - y
    elif y == -mx:
        return start + 2*(byun-1) + x + mx
    else:
        return start + 3*(byun-1) + y + mx

li = []
for i in range(a, c+1):
    lst = []
    li.append(lst)
    for j in range(b, d+1):
        lst.append(get_num(i, j))

mx = 0
for i in li:
    a = max(i)
    if mx < a:
        mx = a
len_ = len(str(mx))

for i in range(len(li)):
    for j in range(len(li[0])):
        s = str(li[i][j])
        length =  len_ - len(s)
        li[i][j] = length * ' ' + s

for i in li:
    print(*i)