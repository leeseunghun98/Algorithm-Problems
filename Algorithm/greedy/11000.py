import sys
N = int(input())
class_list = []
for _ in range(N):
    class_list.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
class_list.sort(key= lambda x:x[0])
cur_time = 0
cnt = 1
li = []
for i in class_list:
    if i[0] >= cur_time:
        cur_time = i[1]
    else:
        cur_time = min(cur_time, i[1])
        cnt += 1
print(cnt)