import sys
n = int(sys.stdin.readline().rstrip('\n'))
roads = list(map(int, sys.stdin.readline().rstrip('\n').split()))
costs = list(map(int, sys.stdin.readline().rstrip('\n').split()))

i = 0
result = 0

while i < n-1:
    if costs[i] < costs[i+1]:
        cost = costs[i]
        idx = i
        while cost < costs[i+1] and i < n-2:
            i += 1
        i += 1
        result += cost * sum(roads[idx:i])
    else:
        result += costs[i] * roads[i]
        i += 1

print(result)