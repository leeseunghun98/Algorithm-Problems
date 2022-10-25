from re import M
import sys
input=sys.stdin.readline
n,m = map(int, input().split())
li = [input().rstrip() for _ in range(n)]
for i in range(n):
    li[i] += li[i]
    li.append(li[i])
answer = [0 for _ in range(26)]
for i in range(2*n):
    for j in range(2*m):
        answer[ord(li[i][j])-65] += (i+1)*(2*n-i)*(j+1)*(2*m-j)
for i in answer:
    print(i)