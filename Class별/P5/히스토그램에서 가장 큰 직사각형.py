import sys
import math
input = sys.stdin.readline

ins = tuple(map(int, input().split()))
# while ins[0] != 0:
#     n = ins[0]
#     ins = ins[1:]
    
    





#     ins = tuple(map(int, input().split()))
n = ins[0]
ins = ins[1:]
tree = [0] * (2 **(math.ceil(math.log(n, 2)+1)))
def segment(left, right, i=1):
    if left == right:
        tree[i] = ins[left]
        return tree[i]
    mid = (left + right) // 2
    tree[i] = segment(left, mid, i*2) + segment(mid+1, right, i*2+1)
    return tree[i]

segment(0, len(ins)-1)
print(tree)