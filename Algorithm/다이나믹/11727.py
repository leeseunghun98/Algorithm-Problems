n = int(input())
li = [[0, 0, 0] for _ in range(1000)]
li[0] = [1, 0, 0]
li[1] = [1, 1, 1]
for i in range(2, 1000):
    li[i] = [sum(li[i-1]), sum(li[i-2]), sum(li[i-2])]
print(sum(li[n-1])%10007)