import sys
input = sys.stdin.readline
n, base_k = map(int, input().split())
num = list(input().rstrip())
stack = []
k = base_k
for i in range(n):

    while k > 0 and stack and num[i] > stack[-1]:
        k-=1
        stack.pop()
    stack.append(num[i])

print("".join(stack[:n-base_k]))