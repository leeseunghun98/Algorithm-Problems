import sys
N = int(sys.stdin.readline().strip())
crane = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
freight = list(map(int, sys.stdin.readline().strip().split()))
crane.sort()
a = crane[-1]
for i in range(N):
    cnt = 0
    for j in freight:
        if crane[i] >= j:
            cnt += 1
    crane[i] = cnt
crane2 = [crane[0]]
for i in range(1, N):
    crane2.append(crane[i] - crane[i-1])
crane2 = crane2[::-1]
cnt = 0
if a < max(freight):
    print(-1)
else:
    while crane2 != ([0] * N):
        for i in range(N):
            for j in range(i, N):
                if crane2[j] != 0:
                    crane2[j] -= 1
                    break
        cnt += 1
    print(cnt)







# import sys
# N = int(sys.stdin.readline().strip())
# crane = list(map(int, sys.stdin.readline().strip().split()))
# M = int(sys.stdin.readline().strip())
# freight = list(map(int, sys.stdin.readline().strip().split()))
# crane.sort()
# freight.sort(reverse=True)
# if crane[-1] < freight[0]:
#     print(-1)
# else:
#     cnt = 0
#     while freight:
#         for i in range(N):
#             for idx, j in enumerate(freight):
#                 if crane[i] >= j:
#                     freight.pop(idx)
#                     break
#         cnt += 1
#     print(cnt)