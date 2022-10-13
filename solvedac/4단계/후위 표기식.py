import sys
s = sys.stdin.readline().rstrip()
stack = []
for i in s:
    if i.isalpha():
        print(i,end="")
    else:
        if i == "(":
            stack.append("(")
        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == '/'):
                print(stack.pop(), end="")
            stack.append(i)
        elif i == "+" or i == "-":
            while stack and stack[-1] != "(":
                print(stack.pop(), end="")
            stack.append(i)
        else:
            while stack and stack[-1] != "(":
                print(stack.pop(), end="")
            stack.pop()
while stack:
    print(stack.pop(), end="")