import sys
n = int(sys.stdin.readline())
li = tuple(map(int, sys.stdin.readline().split()))

lst = []
index_lst = [-1 for _ in range(n)]
max_idx = 0

def mybisect(lst, target):
    start = 0
    finish = len(lst) - 1

    if not lst:
        return 0

    while start < finish:
        mid = (start + finish) // 2
        
        if target <= lst[mid][0]:
            finish = mid - 1
        else:
            start = mid + 1

    if target <= lst[start][0]:
        return start
    return start + 1

for i in range(n):
    idx = mybisect(lst, li[i])
    if idx > 0:
        index_lst[i] = lst[idx-1][1]
    if idx == len(lst):
        lst.append((li[i], i))
        max_idx = i
    else:
        lst[idx] = (li[i], i)

answer = []
while True:
    answer.append(li[max_idx])
    max_idx = index_lst[max_idx]
    if max_idx == -1:
        answer.reverse()
        print(len(lst))
        print(*answer)
        break