# n, m, k = map(int, input().split())
# a = [n + m] + [i for i in range(n-1, -1, -1)]
# dp = [[0 for _ in range(n+m)] for _ in range(n+m)]

# for i in range(n+m):
#     for j in range(n+m):
#         for k in range(i):
#             dp[i][j] += dp[]

# for i in dp:
#     print(i)

# # for i in range(1, n+1):
# #     sm = 1
# #     mem = a[i]
# #     while a[i] + 1 < a[i-1] and k - sm > 0:
# #         a[i] += 1
# #         sm += 