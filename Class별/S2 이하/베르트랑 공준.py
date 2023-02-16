import sys
input = sys.stdin.readline
n = int(input())
li = [1 for _ in range(246913)]
for i in range(2, 123457):
    if li[i]:
        a = 2 * i
        while a < 246913:
            li[a] = 0
            a += i
for i in range(2, 246913):
    li[i] += li[i-1]
    
while n:
    print(li[2*n] - li[n])
    n = int(input())