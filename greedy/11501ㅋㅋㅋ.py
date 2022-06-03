import sys
input = sys.stdin.readline
testcase = int(input().strip())
for _ in range(testcase):
    n = int(input().strip())
    li = list(map(int, input().strip().split()))
    idx = 0
    sm = 0
    while idx < n:
        b = li[idx:].index(max(li[idx:]))
        idx += b
        sm += b * li[idx] - sum(li[idx-b: idx])
        while idx < n-1 and li[idx] == li[idx + 1]:
            idx += 1
        idx += 1
    print(sm)