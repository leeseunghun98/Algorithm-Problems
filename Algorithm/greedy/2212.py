N = int(input())
K = int(input())
li = list(map(int, input().split()))
li = sorted(list(set(li)))
idx = N
for i in range(len(li)):
    if li[i] < 0:
        idx = i
        break
li_plus = li[:idx]
li = sorted(li[idx:])
li.extend(li_plus)
li_gap = [li[i]-li[i-1] for i in range(1, len(li))]
li_gap.sort(reverse=True)
li_gap = li_gap[:K-1]
result = sum(li_gap)
result = li[-1] - li[0] - result
print(result)