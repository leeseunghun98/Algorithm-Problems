import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
nums = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    nums[b] += 1

starts = []
for i in range(1, n+1):
    if nums[i] == 0:
        starts.append(i)

answer = 0
waiting = {}
finish = False

def chk(i):
    if nums[i] == 1:
        starts.append(i)
    else:
        if i in waiting:
            waiting[i] += 1
            if waiting[i] == nums[i]:
                changed.append(i)
        else:
            waiting[i] = 1

while starts and not finish:
    changed = []
    isOne = 0
    if len(starts) == 1:
        answer += 1
        isOne = 1

    while starts:
        j = starts.pop()
        if not graph[j]:
            finish = True
            break
        
        for i in graph[j]:
            chk(i)
        if isOne:
            break
    
    for i in changed:
        starts.append(i)
        del waiting[i]
    
print(answer)