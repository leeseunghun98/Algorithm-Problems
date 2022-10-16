N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key = lambda x:x[0], reverse=True)
result = 0
a = li[0][0]
for i in range(a, 0, -1):
    b = []
    for idx, j in enumerate(li):
        if j[0] >= i:
            b.append([idx, j[1]])
    if b != []:
        b.sort(key = lambda x:x[1], reverse=True)
        c = li.pop(b[0][0])
        result += c[1]
print(result)