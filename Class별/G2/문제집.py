import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
states = [0 for _ in range(n+1)]
lock = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    states[b] += 1
    lock[a].append(b)

nums = []
for i in range(1, n+1):
    if states[i] == 0:
        heapq.heappush(nums, i)

visited = [0 for _ in range(n+1)]
visited[nums[0]] = 1
while nums:
    j = heapq.heappop(nums)
    print(j, end=" ")

    for i in lock[j]:
        states[i] -= 1
        if states[i] == 0 and visited[i] == 0:
            heapq.heappush(nums, i)
            visited[i] = 1