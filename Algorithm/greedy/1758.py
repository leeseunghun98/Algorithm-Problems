import sys
n = int(sys.stdin.readline().strip())
li = [int(sys.stdin.readline().strip()) for _ in range(n)]
li.sort(reverse=True)
idx = 0
result = 0
for i in li:
    if i - idx > 0:
        result += i - idx 
        idx += 1
    else:
        break
print(result)