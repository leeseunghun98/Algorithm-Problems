n = int(input())
li = [0] * 91
li[0], li[1], li[2] = 0, [0, 1], [1, 0]
for i in range(3, 91):
    li[i] = [li[i-1][0]+li[i-1][1], li[i-1][0]]
print(sum(li[n]))