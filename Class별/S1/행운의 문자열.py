s = tuple(input().rstrip())
dic = {}
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
len_ = len(s)
stack = ['0']

if len_ == 10:
    if len(dic) == 10:
        print(3628800)
        exit()

def dfs(prev, depth):
    if depth == len_:
        return 1
    cnt = 0
    for i in dic:
        if dic[i] > 0 and prev != i:
            dic[i] -= 1
            cnt += dfs(i, depth+1)
            dic[i] += 1
    return cnt

print(dfs('0', 0))
