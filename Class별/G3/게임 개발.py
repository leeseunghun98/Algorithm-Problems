import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

building_seq = [0] + [[0, 0, []] for _ in range(n)] # connected num, connected max time, to connect
dp = [0 for _ in range(n+1)]
can_build = deque([])
for building_number in range(1, n+1):
    li = tuple(map(int, input().split()))
    dp[building_number] = li[0]
    building_seq[building_number][0] = len(li)-2
    for i in range(1, len(li)-1):
        building_seq[li[i]][2].append(building_number)
    if len(li) == 2:
        can_build.append(building_number)

while can_build:
    building = can_build.popleft()
    dp[building] += building_seq[building][1]
    for next_build in building_seq[building][2]:
        building_seq[next_build][0] -= 1
        building_seq[next_build][1] = max(building_seq[next_build][1], dp[building])
        if building_seq[next_build][0] == 0:
            can_build.append(next_build)
            
for i in range(1, n+1):
    print(dp[i])