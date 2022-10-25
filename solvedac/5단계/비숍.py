import sys
input = sys.stdin.readline
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

last_idx = n**2
dx = (-1, -1, 1, 1)
dy = (-1, 1, -1, 1)

def is_OK(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        while (0<=nx<n) and (0<=ny<n):
            if li[nx][ny] == 2:
                return False
            nx += dx[i]
            ny += dy[i]
    return True


def dfs(num, cnt):
    x = num // n
    y = num % n

    if num == last_idx:
        return cnt
    
    if li[x][y]:
        if is_OK(x, y):
            li[x][y] = 2
            ret = dfs(num+1, cnt+1)
            li[x][y] = 1
            ret = max(ret, dfs(num+1, cnt))
            return ret
    return dfs(num+1, cnt)

print(dfs(0, 0))