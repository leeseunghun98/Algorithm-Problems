import sys
sys.setrecursionlimit(10**6)
testcase = int(sys.stdin.readline())

def dfs(m, n, visited):
    if m < 0 or m >= y or n < 0 or n >= x:
        return False
    else:
        if visited[m][n] == 0:
            return False
        else:
            visited[m][n] = 0
            dfs(m-1, n, visited)
            dfs(m+1, n, visited)
            dfs(m, n-1, visited)
            dfs(m, n+1, visited)
            return True

for _ in range(testcase):
    
    x, y, n = map(int, sys.stdin.readline().split())
    pos = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    v = [[0 for _ in range(x)] for _ in range(y)]
    
    for b, a in pos:
        v[a][b] = 1
    
    result = 0
    for j in range(y):
        for i in range(x):
            if dfs(j, i, v) == True:
                result += 1
                
    print(result)