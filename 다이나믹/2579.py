n = int(input())
li = [0] * 300
result_li = [[0, 0] for _ in range(300)]
for i in range(n):
    li[i] = int(input())
result_li[0] = [li[0], li[0]]
result_li[1] = [li[0] + li[1], li[1]]
for i in range(2, n):
    result_li[i][0] = result_li[i-1][1] + li[i]
    result_li[i][1] = max(result_li[i-2]) + li[i]
print(max(result_li[n-1]))