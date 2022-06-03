n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
if n == 1:
    print(li[0])
elif n == 2:
    print(li[0] + li[1])
else:
    max_at = [[li[0], li[0], li[0]], [li[1], li[1], li[0] + li[1]], [li[2], li[2] + li[0], max(li[2] + li[1], li[1] + li[0])]]
    for i in range(3, n):
        max_at.append([max(max_at[i-3]) + li[i], max(max_at[i-2]) + li[i], max(max_at[i-1][:2]) + li[i]])
    result = li[0]
    for i in max_at:
        result = max(result, max(i))
    print(result)