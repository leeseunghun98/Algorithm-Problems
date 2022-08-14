import sys
n = int(sys.stdin.readline())
li = [[1, 1], [1, 0]]

def mul_hang(li1, li2):
    lst = [[(li1[0][0]*li2[0][0] + li1[0][1]*li2[1][0])%1000000007, 
            (li1[0][0]*li2[0][1] + li1[0][1]*li2[1][1])%1000000007],
           [(li1[1][0]*li2[0][0] + li1[1][1]*li2[1][0])%1000000007, 
            (li1[1][0]*li2[0][1] + li1[1][1]*li2[1][1])%1000000007]]
    return lst
def solve(lst, v):
    if v == 1:
        return lst
    tmp = solve(lst, v//2)
    if v % 2:
        return mul_hang(mul_hang(tmp, tmp), lst)
    else:
        return mul_hang(tmp, tmp)
if n < 2:
    print(n)
else:
    print(solve(li, n-1)[0][0])