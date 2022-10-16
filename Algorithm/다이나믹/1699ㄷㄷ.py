# n = int(input())
# dp = [i for i in range(n+1)]
# for i in range(2, n+1):
#     a = 1
#     while i >= a*a:
#         if dp[i] > dp[i - a*a] + 1:
#             dp[i] = dp[i - a*a] + 1
#         a += 1
# print(dp[n])


# # # ㄷㄷ;;
# n=int(input())
# q={i*i for i in range(1,int(n**.5)+1)}
# a={n-i for i in q}
# b={i-j for i in a for j in q}
# print(q)
# print(a)
# print(b)
# print(q&b)
# if 0 in a:print(1)
# elif 0 in b:print(2)
# elif q&b:print(3)
# else:print(4)