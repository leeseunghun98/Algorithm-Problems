import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
li = tuple(map(int, input().split()))
stack = [li[0]]
for i in li[1:]:
    if stack[-1] < i:
        stack.append(i)
        continue
    idx = bisect_left(stack, i)
    stack[idx] = i
print(len(stack))