from itertools import combinations

N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]
chickens = []
homes = []
for i in range(N):
    for j in range(N):
        if li[i][j] == 1:
            homes.append((i, j))
        elif li[i][j] == 2:
            chickens.append((i, j))

# def combination(lst, m):
#     for i in range(len(lst)):
#         if m == 1:
#             yield [lst[i]]
#         else:
#             for next in combination(lst[i+1:], m-1):
#                 yield [lst[i]] + next

answer = float("inf")
for chicken in combinations(chickens, M):
    chi_dis = 0
    for i in homes:
        res = 2 * N
        for j in chicken:
            dis = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if dis < res:
                res = dis
        chi_dis += res
    if chi_dis < answer:
        answer = chi_dis

print(answer)