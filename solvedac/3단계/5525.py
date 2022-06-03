import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip()
a = 'I' + 'OI' * n
result = 0
for i in range(len(s) - 2*n):
    if s[i:i+2*n+1] == a:
        result += 1
print(result)