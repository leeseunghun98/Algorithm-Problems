import sys
input = sys.stdin.readline
r, c = map(int, input().split())
li = [list(input().rstrip()) for _ in range(r)]
chk = lambda x : True if (0<=x<r) else False

def dfs(x, y):
    li[x][y] = 'x'
    if y == c-1:
        return 1
    if x > 0 and li[x-1][y+1] == '.' and dfs(x-1, y+1):
        return 1
    if li[x][y+1] == '.' and dfs(x, y+1):
        return 1
    if x+1 < r and li[x+1][y+1] == '.' and dfs(x+1, y+1):
        return 1
    return 0

answer = 0
for x in range(r):
    answer += dfs(x, 0)
print(answer)