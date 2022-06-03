import sys
a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())
while len(b) != len(a):
    if b[-1] == 'A':
        b.pop(-1)
    else:
        b.pop(-1)
        b = b[::-1]
print(1 if b == a else 0)