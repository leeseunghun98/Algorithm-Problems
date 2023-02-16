import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = tuple(map(int, input().split()))

answer = 0
stack = [(0, li[0])]
for i in range(1, m):
    while stack and stack[-1][1] <= li[i]:
        idx, height = stack.pop()
        if stack:
            answer += (min(stack[-1][1], li[i]) - height) * (i - 1 - stack[-1][0])
    stack.append((i, li[i]))
print(answer)