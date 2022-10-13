import sys
input = sys.stdin.readline
s = input().rstrip()
explosion = list(input().rstrip())
stack = []
for i in s:
    stack.append(i)
    if len(stack) >= len(explosion) and stack[len(stack) - len(explosion):] == explosion:
        for _ in range(len(explosion)):
            stack.pop()
print("".join(stack) if len(stack) > 0 else "FRULA")