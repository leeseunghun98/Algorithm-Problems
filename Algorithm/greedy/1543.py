import sys
a = sys.stdin.readline().rstrip('\n')
b = sys.stdin.readline().rstrip('\n')
n = 0
cnt = 0
while n < len(a):
    if a[n:n+len(b)] == b:
        cnt += 1
        n += len(b)
    else:
        n += 1
print(cnt)