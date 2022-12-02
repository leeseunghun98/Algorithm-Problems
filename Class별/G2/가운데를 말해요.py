import sys
import heapq
input = sys.stdin.readline
testcase = int(input())

lower = []
higher = []
cnt = 1
# 홀수번째에 넣고 나서 len(lower) += 1, 짝수번째 넣고 나서 len(higher) += 1
for _ in range(testcase):
    n = int(input())
    
    if cnt % 2: # 홀수번째
        if not lower:
            lower.append(-n)
        else:
            if n > higher[0]:
                heapq.heappush(lower, -heapq.heappop(higher))
                heapq.heappush(higher, n)
            else:
                heapq.heappush(lower, -n)
        print(-lower[0])
    else: # 짝수번째
        if n >= -lower[0]:
            heapq.heappush(higher, n)
        else:
            heapq.heappush(higher, -heapq.heappop(lower))
            heapq.heappush(lower, -n)
        print(min(-lower[0], higher[0]))

    cnt += 1