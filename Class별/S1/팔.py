l, r = map(int, input().split())
stl = list(str(l))
idxs = []
for i in range(len(stl)):
    if stl[i] == '8':
        idxs.append(i)

def dfs(idx):
    if idx == len(idxs):
        return stl.count('8')
    cnt = 9
    tmp = stl[idxs[idx]]
    for i in range(7, 10):
        stl[idxs[idx]] = str(i)
        if (l<=int(''.join(stl))<=r):
            cnt = min(cnt, dfs(idx+1))
    stl[idxs[idx]] = tmp
    return cnt

print(dfs(0))