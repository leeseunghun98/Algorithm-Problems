n = int(input())
di = list(map(int, input().split()))
if n == 1:
    print(sum(di) - max(di))
else:
    min2 = min(di[0]+di[1], di[0]+di[2], di[0]+di[3], di[0]+di[4], di[1]+di[2], di[1]+di[3],
               di[2]+di[4], di[2]+di[5], di[3]+di[4], di[3]+di[5], di[4]+di[5], di[5]+di[1])
    min3 = min(di[0]+di[1]+di[2], di[0]+di[1]+di[3], di[0]+di[2]+di[4], di[0]+di[3]+di[4],
               di[5]+di[1]+di[2], di[5]+di[1]+di[3], di[5]+di[2]+di[4], di[5]+di[3]+di[4])
    print((n-2)*(5*n-6)*min(di) + (8*n -12)*min2 + 4 * min3)
    