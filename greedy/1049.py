N, M = map(int, input().split())
setli = []
li = []
for _ in range(M):
    a, b = map(int, input().split())
    setli.append(a)
    li.append(b)
setli.sort()
li.sort()

result = 0
if li[0]*6 < setli[0]:
    result = li[0] * N
elif (N % 6)*li[0] > setli[0]:
    result = (N // 6 + 1) * setli[0]
else:
    result = (N // 6 * setli[0]) + N % 6 * li[0]   

print(result)