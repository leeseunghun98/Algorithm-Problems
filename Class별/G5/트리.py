import sys
input = sys.stdin.readline
n = int(input())
li = tuple(map(int, input().split()))
erase = int(input())
dic = {}
for i in range(n):
    if li[i] not in dic:
        dic[li[i]] = [i]
    else:
        dic[li[i]].append(i)
dic[li[erase]].remove(erase)
if len(dic[li[erase]]) == 0:
    del dic[li[erase]]
    
def findTree(root):
    if root not in dic:
        return 1
    ret = 0
    for next in dic[root]:
        ret += findTree(next)
    return ret

root = li.index(-1)
print(findTree(-1) if erase != root else 0)