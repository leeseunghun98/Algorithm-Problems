import sys
n = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))
result = 0
idx = 0
for i in li:
    if i == idx:
        result += 1
        if idx == 2:
            idx = 0
        else:
            idx += 1
print(result)