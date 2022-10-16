n = int(input())
li = list(map(int, input().split()))
result = [0] * n
for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            if result[i] < result[j]:
                result[i] = result[j]
    result[i] += 1
print(max(result))