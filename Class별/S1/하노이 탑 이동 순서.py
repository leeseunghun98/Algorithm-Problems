n = int(input())
print(2**n-1)

def moving(s, t, v, num):
    if num == 1:
        print(s, t)
        return
    moving(s, v, t, num-1)
    print(s, t)
    moving(v, t, s, num-1)

moving(1, 3, 2, n)