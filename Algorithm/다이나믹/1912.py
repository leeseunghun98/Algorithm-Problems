n = int(input())
li = list(map(int, input().split()))
result = [li[0]]
for i in range(n-1):
    result.append(max(li[i+1], result[i] + li[i+1]))
print(max(result))