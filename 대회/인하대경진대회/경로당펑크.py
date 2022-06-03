import sys
n = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())
J_li = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
M_li = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']
if s[-2] in M_li and s[-1] in J_li:
    print(1)
else:
    print(0)