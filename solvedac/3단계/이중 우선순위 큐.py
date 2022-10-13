import sys
import heapq
testcase = int(sys.stdin.readline())

def delete_dic(queue, num):
    while queue and num*queue[0] not in dic:
        heapq.heappop(queue)
    if queue:
        dic[num * queue[0]] -= 1
        if dic[num * queue[0]] == 0:
            del dic[num * queue[0]]
        while queue and num * queue[0] not in dic:
            heapq.heappop(queue)
for _ in range(testcase):
    n = int(sys.stdin.readline())
    queue_min = []
    queue_max = []
    dic = {}
    for _ in range(n):
        operater, num = sys.stdin.readline().split()
        num = int(num)
        if operater == 'I':
            heapq.heappush(queue_min, num)
            heapq.heappush(queue_max, -num)
            if dic.get(num, 0) == 0:
                dic[num] = 1
            else:
                dic[num] += 1
        else:
            if num == -1:
                delete_dic(queue_min, -num)
            else:
                delete_dic(queue_max, -num)
    if dic == {}:
        print("EMPTY")
    else:
        print(max(dic), min(dic))