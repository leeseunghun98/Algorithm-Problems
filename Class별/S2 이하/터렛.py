import sys
import math
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    
    if r1 < r2:
        tmp = r1
        r1 = r2
        r2 = tmp
    
    if dist > r1 + r2:
        print(0)
    elif dist == r1 + r2 or dist == r1 - r2:
        print(1)
    elif (r1 - r2 < dist < r1 + r2):
        print(2)
    else:
        print(0)