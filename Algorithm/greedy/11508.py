import sys
n = int(sys.stdin.readline().strip())
li = [int(sys.stdin.readline().strip()) for _ in range(n)]
li.sort(reverse=True)
result = 0
for i in range(n):
    if i % 3 == 2:
        continue
    else:
        result += li[i]
print(result)