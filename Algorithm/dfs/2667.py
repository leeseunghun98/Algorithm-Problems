n = int(input())
town = []

for i in range(n):
  town.append(list(map(int, list(input()))))

def dfs(x, y, cnt):
  if x <= -1 or x >= n or y <= -1 or y >= n:
    return False
  if town[x][y] == 1:
    cnt.append(1)
    town[x][y] = 0

    dfs(x-1, y, cnt)
    dfs(x, y-1, cnt)
    dfs(x+1, y, cnt)
    dfs(x, y+1, cnt)
    return True
  return False

cnt = []
a = []
for i in range(n):
  for j in range(n):
    if dfs(i, j, cnt) == True:
      dfs(i, j, cnt)
      a.append(len(cnt))
      cnt = []
      
print(len(a))
for v in sorted(a):
  print(v)