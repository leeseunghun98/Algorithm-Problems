N = int(input())
pi = list(map(int, input().split()))
li = [0] * N
for i in range(N):
    li[i] = pi[i]
for i in range(1, N):
    for j in range(i):
        li[i] = max(li[i], li[j] + pi[i-j-1])
print(li[-1])