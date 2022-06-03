import sys
li = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0
if li[0] == 0 and li[1] == 0:
    print(0)
else:
    if li[0] == 0:
        li[0] = 1
        cnt += 1
    while li[0] * 2 <= li[1]:
        li[0] *= 2
        cnt += 1
    while (li[0] - 1) * 2 >= li[1]:
        li[0] -= 1
        cnt += 1
    print(cnt, li[0])
    if li[0] * 2 - li[1] < li[1] - li[0]:
        print(cnt + li[0] * 2 - li[1] + 1)
    else:
        print(cnt + li[1] - li[0])

# import sys
# li = sorted(list(map(int, sys.stdin.readline().split())))
# cnt = 0
# if li[0] == 0 and li[1] == 0:
#     print(0)
# else:
#     if li[0] == 0:
#         li[0] = 1
#         cnt += 1
#     while li[1] // 2 >= li[0]:
#         cnt += 1
#         if li[1] % 2 == 0:
#             li[1] //= 2
#         else:
#             li[1] -= 1
#     if li[1] % 2 == 0:
#         if li[1] // 2 == li[0]:
#             print(cnt + 1)
#         elif li[1] - li[0] <= (li[0] - li[1] // 2):
#             print(cnt + li[1] - li[0])
#         else:
#             print(cnt + 1 + li[0] - li[1] // 2)
#     else:
#         if li[1] - 1 == li[0]:
#             print(cnt + 1)
#         elif li[1] - li[0] <= (li[1] - 1) // 2 - li[0] + 1:
#             print(cnt + li[1] - li[0])
#         else:
#             print(cnt + 2 + li[0] - (li[1] - 1) // 2)