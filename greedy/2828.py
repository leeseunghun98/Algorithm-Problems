import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
apps = int(input().strip())
apples = [int(input().strip()) for _ in range(apps)]
pos_left = 1
pos_right = M
result = 0
for i in apples:
    if i < pos_left:
        p = pos_left - i
        result += p
        pos_left -= p
        pos_right -= p
    elif i > pos_right:
        p = i - pos_right
        result += p
        pos_left += p
        pos_right += p
print(result)