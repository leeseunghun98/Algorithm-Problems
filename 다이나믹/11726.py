li = [0] * 1001
li[1] = 1
li[2] = 2
for i in range(3, 1001):
    li[i] = li[i-1] + li[i-2]
print(li[int(input())]%10007)