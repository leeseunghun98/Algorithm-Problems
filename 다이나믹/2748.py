n = int(input())
li = [0] * 91
li[1], li[2] = 1, 1
for i in range(3, 91):
    li[i] = li[i-1] + li[i-2]
print(li[n])