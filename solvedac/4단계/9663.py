n = int(input())
li = [-1 for _ in range(n)]

def dfs(x, y):
    li[y] = x
    for i in range(n):
        one = 0
        for j in range(1, y+2):
            if li[y+1-j] == i+j or li[y+1-j] == i or (i-j > -1 and li[y+1-j] == i-j):
                one = 1
                break
        if one == 1:
            continue
        elif y == n-2:
            global result
            result += 1
        else:
            dfs(i, y+1)
    li[y] = -1

result = 0
for i in range(n):
    dfs(i, 0)
print(result if n > 1 else 1)