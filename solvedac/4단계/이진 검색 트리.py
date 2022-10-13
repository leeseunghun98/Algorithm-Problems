import sys
from bisect import bisect_left
sys.setrecursionlimit(10**6)
li = []
cnt = 0
while True:
    try:
        num = int(sys.stdin.readline())
        li.append(num)
    except:
        break
n = len(li)
postorder = []
def preorder(idx, fin):
    postorder.append(li[idx])
    if idx == fin:
        return
    right = 0
    for index, i in enumerate(li[idx+1: fin+1]):
        if i > li[idx]:
            right = index + idx + 1
            break
    if right != 0:
        preorder(right, fin)
    if right != 0 and idx + 1 < right:
        preorder(idx+1, right-1)
    if right == 0:
        preorder(idx+1, fin)

preorder(0, n-1)
postorder.reverse()
print(*postorder)