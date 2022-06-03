import sys
n, k = map(int, sys.stdin.readline().strip().split())
li = list(map(int, sys.stdin.readline().strip().split()))
li_sub = [0] * (n-1)
for i in range(n-1):
    li_sub[i] = li[i+1] - li[i]
li_sub.sort()
print(sum(li_sub[:n-k]))