levels = int(input())
level = []
for _ in range(levels):
    level.append(int(input()))
result = 0
level = level[::-1]
for j in range(len(level) - 1):
    if level[j] <= level[j+1]:
        gap = level[j+1] - level[j] + 1
        level[j+1] -= gap
        result += gap
print(result)