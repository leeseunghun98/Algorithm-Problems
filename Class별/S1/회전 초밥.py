import sys
input = sys.stdin.readline
n, d, k, coupon = map(int, input().split())
trail = [int(input()) for _ in range(n)]
trail += trail[:k-1]
chobob = [0 for _ in range(d+1)]
chobobss = 0
chobob[coupon] += 1
chobobss += 1
for i in range(k):
    if not chobob[trail[i]]:
        chobobss += 1
    chobob[trail[i]] += 1
cur_chobobss = chobobss
for i in range(n-1):
    chobob[trail[i]] -= 1
    if chobob[trail[i]] == 0:
        cur_chobobss -= 1
    if chobob[trail[i+k]] == 0:
        cur_chobobss += 1
    chobob[trail[i+k]] += 1
    if cur_chobobss > chobobss:
        chobobss = cur_chobobss
print(chobobss)