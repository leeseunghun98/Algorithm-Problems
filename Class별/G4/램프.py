import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = [list(map(int, list(input().rstrip()))) for _ in range(n)]
k = int(input())
def chk(row):
    zeros = [0 for _ in range(m)]
    for i in range(m):
        if li[row][i] == 0:
            zeros[i] = 1
    column = [1 for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if zeros[i]:
                if li[j][i] == 0 and column[j]:
                    continue
                else:
                    column[j] = 0
            else:
                if li[j][i] and column[j]:
                    continue
                column[j] = 0
    return column.count(1)

answer = 0
for i in range(n):
    cnt = li[i].count(0)
    if cnt > k:
        continue
    a = (k - cnt) % 2
    if a == 0:
        answer = max(answer, chk(i))
print(answer)