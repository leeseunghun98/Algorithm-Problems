import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
testcase = int(input())

def chk(start):
    global i
    visited[start] = i
    next = li[start]
    if visited[next] == 0:
        cross = chk(next)
        if not cross:
            return False
        li[start] = 0
        if start == cross:
            return False
        return cross
    if visited[next] == i:
        li[start] = 0
        if start == next:
            return False
        return next
    return False
    
for _ in range(testcase):
    n = int(input())
    li = [0] + list(map(int, input().split()))
    idx = 0
    visited = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if li[i] != 0:
            chk(i)
    print(n+1-li.count(0))