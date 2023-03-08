import sys
from collections import defaultdict, deque
input = sys.stdin.readline
n = 3
puzzle = ""
boundary = lambda x : True if (0<=x<9) else False
for _ in range(n):
    puzzle += str(input().replace(" ", "").rstrip())
dic = defaultdict(bool)
dic[puzzle] = True
queue = deque([(puzzle, 0)])
answer = -1
switches = [(1, 3), (-1, 1, 3), (-1, 3), (-3, 1, 3), (-3, -1, 1, 3), (-3, -1, 3), (-3, 1), (-3, -1, 1), (-3, -1)]

def changedString(s, x, zero_idx):
    ret = list(s)
    ret[zero_idx] = ret[x]
    ret[x] = "0"
    return "".join(ret)

while queue:
    j, cnt = queue.popleft()
    if j == "123456780":
        answer = cnt
        break
    zero_pos = j.index("0")
    for i in switches[zero_pos]:
        if boundary(zero_pos + i):
            cString = changedString(j, zero_pos+i, zero_pos)
            if not dic[cString]:
                queue.append((cString, cnt+1))
                dic[cString] = True
print(answer)