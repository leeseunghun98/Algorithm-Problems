import sys
N = int(sys.stdin.readline().strip())
li = [int(sys.stdin.readline().strip()) for _ in range(N)]
li.sort()
sum = 0
for i in range(N):
    sum += ((li[i] - (i+1)) if li[i]-(i+1) > 0 else i+1-li[i])
print(sum)