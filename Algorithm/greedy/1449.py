N, L = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
cur = 0
result = 0
for i in li:
    if cur < i:
        cur = i - 0.5 + L
        result += 1
print(result)