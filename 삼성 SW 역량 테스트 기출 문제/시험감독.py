n = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())
answer = n
for i in range(n):
    Ai[i] -= B
    if Ai[i] > 0:
        remain = ((Ai[i] % C) > 0)
        if remain == 1:
            answer += 1
        answer += (Ai[i] // C)
print(answer)