import sys
n = int(sys.stdin.readline().strip())
li = [int(sys.stdin.readline().strip()) for _ in range(n)]
li.sort(reverse=True)
zero_idx = -1
li_minus = []
for i in range(n):
    if li[i] <= 0:
        zero_idx = i
        break
li_zero = 0
if zero_idx >= 0 and li[zero_idx] == 0:
    li_zero = 1
if zero_idx >= 0:
    if li_zero == 1:
        li_minus = li[zero_idx+1:]
    else:
        li_minus = li[zero_idx:]
if zero_idx >= 0:
    li = li[:zero_idx]
one_idx = -1
for i in range(len(li)):
    if li[i] == 1:
        one_idx = i
        break
li_ones = 0
if one_idx >= 0:
    li_ones = sum(li[one_idx:])
    li = li[:one_idx]
result = 0
li_minus.sort()
for i in range(0, len(li), 2):
    if i+1 < len(li):
        result += li[i] * li[i+1]
for i in range(0, len(li_minus), 2):
    if i+1 < len(li_minus):
        result += li_minus[i] * li_minus[i+1]
if len(li) % 2 == 1:
    result += li[-1]
if len(li_minus) % 2 == 1:
    if li_zero == 0:
        result += li_minus[-1]
result += li_ones
print(result)