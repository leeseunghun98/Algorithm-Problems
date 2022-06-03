i = 1
while True:
    L, P, V = map(int, input().split())
    if(L == P == V == 0):
        break
    if V%P > L:
        print("Case {}: {}".format(i, (V//P)*L + L))
    else:
        print("Case {}: {}".format(i, (V//P)*L + V%P))    
    i += 1