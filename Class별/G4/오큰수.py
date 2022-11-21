import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
answers = [-1 for _ in range(n)]

queue = [A[-1]]
for i in range(n-2, -1, -1):
    while queue and A[i] >= queue[-1]:
        queue.pop()
    if queue:
        answers[i] = queue[-1]
    queue.append(A[i])
print(*answers)