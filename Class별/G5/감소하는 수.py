from collections import deque
n = int(input())
if n == 0:
    print(0)
    exit()
mx_num = 9876543210
mx_len = 9
answer, ret = 0, 1
queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
while queue:
    j = queue.popleft()
    answer += 1
    if answer == n:
        ret = 0
        print(j)
        break
    can_next = j % 10
    for i in range(can_next):
        queue.append(j*10+i)
if ret:
    print(-1)