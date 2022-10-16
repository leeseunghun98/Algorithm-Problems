import sys
n = int(sys.stdin.readline().rstrip('\n'))

lst = []
for i in range(n):
    lst.append(sys.stdin.readline().rstrip('\n'))
alpha = []
for i in lst:
    for j in i:
        if j not in alpha:
            alpha.append(j)

dic = [[] for _ in range(8)]

for aaa in lst:
    for idx, c in enumerate(aaa[::-1]):
        dic[idx].append(c)

a = [0 for _ in range(10)]

for index, al in enumerate(alpha):
    for idx, i in enumerate(dic):
        for j in i:
            if al == j:
                a[index] += (10  ** idx)

a.sort(reverse=True)
result = 0
for idx, i in enumerate(a):
    result += (9-idx) * i
print(result)