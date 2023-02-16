import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]

stack = []
stack_number = 1
answer = []
for i in li:
    if i > stack_number:
        for j in range(stack_number, i):
            stack.append(j)
            answer.append('+')
        answer.append('+')
        answer.append('-')
        stack_number = i+1
    elif i == stack_number:
        stack_number += 1
        answer.append('+')
        answer.append('-')
    else:
        if stack and stack[-1] == i:
            stack.pop()
            answer.append('-')
        else:
            answer = ['NO']
            break
    if answer[0] == 'NO':
        break
for i in answer:
    print(i)