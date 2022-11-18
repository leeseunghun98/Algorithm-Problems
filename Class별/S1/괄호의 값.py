s = input().rstrip()
stack = []
for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        ret = 0
        while True:
            if i == ')':
                if stack and stack[-1] == '(':
                    ret *= 2
                    if ret == 0:
                        ret = 2
                    stack.pop()
                    stack.append(ret)
                    break 
                if not stack:
                    stack = [0]
                    break
            else:
                if stack and stack[-1] == '[':
                    ret *= 3
                    if ret == 0:
                        ret = 3
                    stack.pop()
                    stack.append(ret)
                    break
                if not stack:
                    stack = [0]
                    break
            a = stack.pop()
            if a == '[' or a == '(':
                stack = [0]
                break
            ret += a
    if stack == [0]:
        break
if '(' in stack or '[' in stack:
    print(0)
else:
    print(sum(stack))