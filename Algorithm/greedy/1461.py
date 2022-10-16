import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
li = list(map(int, input().strip().split()))
while 0 in li:
    li.remove(0)
li.sort()
q = max(abs(li[0]), abs(li[-1]))
result = 0
while li:
    idx = 0
    if abs(li[0]) > abs(li[-1]):
        a = li.pop(0)
        b = 0
        while li and idx < M-1:
            idx += 1
            if a * li[0] < 0:
                break
            b = li.pop(0)
    else:
        a = li.pop(-1)ㄴㄴㄴㄴ
        while li and idx < M-1:
            idx += 1
            if a * li[-1] < 0:
                break
            b = li.pop(-1)
    result += abs(a) * 2
print(result-q)