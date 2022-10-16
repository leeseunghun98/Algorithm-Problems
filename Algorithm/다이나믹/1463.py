N = int(input())
li = [0] * 1000001
def f(n):
    min_list = []
    if n % 3 == 0:
        min_list.append(li[n//3] + 1)
    if n % 2 == 0:
        min_list.append(li[n//2] + 1)
    min_list.append(li[n-1] + 1)
    li[n] = min(min_list)
for i in range(1, N+1):
    f(i)
print(li[N]-1)