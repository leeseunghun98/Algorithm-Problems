import sys
input = sys.stdin.readline
n = int(input().rstrip())
s = tuple(input().rstrip())
nums = tuple(map(int, s[::2]))
opers = s[1::2]
l = len(opers)
answer = -float("INF")

def dfs(idx, ret):
    global answer
    if idx >= l:
        answer = max(answer, ret)
        return
    if idx < l-1:
        dfs(idx+2, cal(opers[idx], ret, cal(opers[idx+1], nums[idx+1], nums[idx+2])))
    dfs(idx+1, cal(opers[idx], ret, nums[idx+1]))
    
def cal(operand, a, b):
    if operand == '*':
        return a * b
    elif operand == '+':
        return a + b
    else:
        return a - b

dfs(0, nums[0])
print(answer)