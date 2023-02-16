import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
li = [0] + [int(input()) for _ in range(n)]

visited = [0 for _ in range(n+1)]
answers = []
for i in range(1, n+1):
    num = i
    while visited[num] != i:
        visited[num] = i
        num = li[num]
    if num == i:
        answers.append(i)
print(len(answers))
for i in answers:
    print(i)
