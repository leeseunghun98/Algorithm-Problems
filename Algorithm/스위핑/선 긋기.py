import sys
input = sys.stdin.readline
n = int(input())
prev = -int(1e9)
answer = 0
li = []
for _ in range(n):
    a, b = map(int, input().split())
    li.append((a, b))
li.sort()

for i in li:
    a, b = i
    if b <= prev:
        continue
    elif a <= prev:
        answer += b - prev
    else:
        answer += b - a
    prev = b
    
print(answer)