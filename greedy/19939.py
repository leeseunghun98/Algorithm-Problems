import sys
n, k = map(int, sys.stdin.readline().strip().split())
li = [i+1 for i in range(k)]
if sum(li) > n:
    print(-1)
else:
    while sum(li) < n:
        li = [i+1 for i in li]
    if sum(li) - n > 0:
        print(k)
    else:
        print(k-1)