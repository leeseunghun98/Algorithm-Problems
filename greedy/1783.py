N, M = map(int, input().split())
if M == 1 or N == 1:
    print(1)
elif N == 2:
    if M < 9:
        print(1 + (M - 1)//2)
    else:
        print(4)
else:
    if M > 6:
        print(M-2)
    elif M <= 4:
        print(M)
    else:
        print(4)