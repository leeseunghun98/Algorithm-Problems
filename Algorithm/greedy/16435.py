import sys
n, L = map(int, sys.stdin.readline().strip().split())
li = list(map(int, sys.stdin.readline().strip().split()))
li.sort()
for i in li:
    if i <= L:
        L += 1
    else:
        break
print(L)