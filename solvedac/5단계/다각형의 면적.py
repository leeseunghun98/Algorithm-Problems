import sys
input = sys.stdin.readline
n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]
dots.append(dots[0])
answer = 0
for i in range(n):
    answer += dots[i][0] * dots[i+1][1] - dots[i][1] * dots[i+1][0]
answer /= 2
print(round(abs(answer),1))
