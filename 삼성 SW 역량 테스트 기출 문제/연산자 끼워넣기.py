N = int(input())
Ai = tuple(map(int, input().split()))
operands = list(map(int, input().split()))
mn = float("inf")
mx = -float("inf")
len_ = len(Ai)
def solve(Ai, operands, idx, result, len_):
    global mn
    global mx
    if idx == len_:
        if result > mx:
            mx = result
        if result < mn:
            mn = result
    for i in range(4):
        if operands[i] > 0:
            res = result
            if i == 0:
                res += Ai[idx]
            elif i == 1:
                res -= Ai[idx]
            elif i == 2:
                res *= Ai[idx]
            else:
                re = 0
                if res < 0:
                    re += 1
                if Ai[idx] < 0:
                    re += 1
                if re > 0:
                    res = abs(res) // abs(Ai[idx])
                    res = -res
                else:
                    res //= Ai[idx]
                    
            operands[i] -= 1
            solve(Ai, operands, idx + 1, res, len_)
            operands[i] += 1
solve(Ai, operands, 1, Ai[0], len_)
print(mx)
print(mn)