import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
st = sorted(list(set(li)))
dic = {}
for i in range(len(st)):
    dic[st[i]] = i
for i in li:
    print(dic[i], end=" ")
# 아래 오히려 시간 더걸림, 메모리는 덜먹음
# import sys
# import heapq
# n = int(sys.stdin.readline())
# li = list(map(int, sys.stdin.readline().split()))
# st = list(set(li))
# heapq.heapify(st)
# dic = {}
# for i in range(len(st)):
#     dic[heapq.heappop(st)] = i
# for i in li:
#     print(dic[i], end=" ")