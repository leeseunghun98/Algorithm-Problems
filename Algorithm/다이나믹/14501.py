import sys
n = int(sys.stdin.readline().strip())
li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
result = [0] * (n+1)
for i in range(n+1):
    for j in range(i):
        if li[j][0] + j <= i:
            result[i] = max(result[i], result[j] + li[j][1])
print(max(result))