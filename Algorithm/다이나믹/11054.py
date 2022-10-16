import sys
len_ = int(sys.stdin.readline().strip())
li = list(map(int, sys.stdin.readline().strip().split()))
dp_inc = [0] * len_
dp_dec = [0] * len_
dp_inc[0] = 1
dp_dec[-1] = 1
for i in range(1, len_):
    mx = 1
    for j in range(i):
        if li[j] < li[i]:
            mx = max(mx, dp_inc[j] + 1)
    dp_inc[i] = mx
for i in range(len_-1, -1, -1):
    mx = 1
    for j in range(len_-1, i, -1):
        if li[j] < li[i]:
            mx = max(mx, dp_dec[j] + 1)
    dp_dec[i] = mx
for i in range(len_):
    dp_inc[i] += dp_dec[i]
print(max(dp_inc) - 1)