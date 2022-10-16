N = int(input())
li = [[0]*10 for _ in range(N)]
for i in range(10):
    li[0][i] = 1
for i in range(1, N):
    for j in range(10):
        li[i][j] = sum(li[i-1][:j+1]) % 10007
print(sum(li[N-1]) % 10007)