N = int(input())
li = [[0, 0]] * 41
li[0] = [1, 0]
li[1] = [0, 1]
n = []
for i in range(2, 41):
    li[i] = [li[i-1][0] + li[i-2][0], li[i-1][1] + li[i-2][1]]
for _ in range(N):
    n.append(int(input()))
for i in n:
    print(li[i][0], li[i][1])