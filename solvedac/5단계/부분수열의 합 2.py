import sys
from itertools import combinations
from collections import Counter

input = sys.stdin.readline
n, s = map(int, input().split())
li = list(map(int, input().split()))

def get(lst):
    sums = []
    for len_ in range(1, len(lst)+1):
        for i in combinations(lst, len_):
            sums.append(sum(i))
    return sorted(sums)

half = n//2
li1 = li[:half]
li2 = li[half:]
sumli1 = get(li1)
sumli2 = get(li2)
answer = 0
li1_counter = Counter(sumli1)
li2_counter = Counter(sumli2)

for i in sumli1:
    target = s - i
    # Counter를 이용
    answer += li2_counter[s-i]
answer += li1_counter[s]
answer += li2_counter[s]
print(answer)

# import sys
# from itertools import combinations
# from bisect import bisect_left, bisect_right
# input = sys.stdin.readline
# n, s = map(int, input().split())
# li = list(map(int, input().split()))

# def get(lst):
#     sums = []
#     for len_ in range(1, len(lst)+1):
#         for i in combinations(lst, len_):
#             sums.append(sum(i))
#     return sorted(sums)

# half = n//2
# li1 = li[:half]
# li2 = li[half:]
# sumli1 = get(li1)
# sumli2 = get(li2)
# answer = 0
# for i in sumli1:
#     target = s - i
#     # 정렬된 것 bisect로 개수 확인, 해당 개수만큼 +
#     answer += bisect_right(sumli2, target) - bisect_left(sumli2, target)
# answer += bisect_right(sumli1, s) - bisect_left(sumli1, s)
# answer += bisect_right(sumli2, s) - bisect_left(sumli2, s)
# print(answer)