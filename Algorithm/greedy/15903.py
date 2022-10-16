n, m = map(int, input().split())
li = list(map(int, input().split()))
for _ in range(m):
    li.sort()
    a = li[0] + li[1]
    li[0] = a
    li[1] = a
print(sum(li))