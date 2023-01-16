import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = list(map(int, input().split()))
a = [0 for _ in range(m)]
b = 0
for i in range(n):
    b += li[i]
    a[b % m] += 1
answer = a[0]
for v in a:
    answer += v*(v-1)//2
print(answer)

# import sys
# from collections import Counter
# input = sys.stdin.readline
# n, m = map(int, input().split())
# li = list(map(int, input().split()))
# for i in range(1, n):
#     li[i] = (li[i-1] + li[i]) % m
# li = Counter(li)
# answer = li[0]
# for v in li.values():
#     answer += v*(v-1)//2
# print(answer)