# def solve(n):
#     odds = []
#     evens = []
#     re = 0
#     for i in range(1, n+1):
#         if re < 8:
#             odds.append(i)
#             re += 1
#         else:
#             evens.append(i)
#             re += 1
#             if re == 16:
#                 re = 0
#     print(*odds, sep=",")
#     print(*evens, sep=",")
    








# if __name__ == "__main__":
#     n = int(input())
#     solve(n)


def f(x, l=[]):
    for i in range(x):
        l.append(i)
    print(l)


f(2)
f(3, [1, 2, 3])
f(2)