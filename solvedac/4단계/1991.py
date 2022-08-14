import sys
n = int(sys.stdin.readline())
li = [0] * (n+1)
for i in range(n):
    a, b, c = map(ord, sys.stdin.readline().split())
    li[a-64] = [b-64, c-64]
def first(start):
    print(chr(start + 64), end="")
    if li[start][0] > 0:
        first(li[start][0])
    if li[start][1] > 0:
        first(li[start][1])
def second(start):
    if li[start][0] < 0:
        print(chr(start+64), end="")
    else:
        second(li[start][0])
        print(chr(start+64), end="")
    if li[start][1] > 0:
        second(li[start][1])
def third(start):
    if li[start][0] > 0:
        third(li[start][0])
    if li[start][1] > 0:
        third(li[start][1])
    print(chr(start+64), end="")
first(1)
print()
second(1)
print()
third(1)