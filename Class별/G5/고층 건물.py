import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))

def solve(pos):
    left = pos - 1
    right = pos + 1
    ret = 0
    if left >= 0:
        left_l = li[pos] - li[left]
        ret += 1
    else:
        left = -1
    if right < n:
        right_l = li[right] - li[pos]
        ret += 1
    else:
        right = n
    while left >= 0:
        newleft_l = (li[pos] - li[left]) / (pos - left)
        left_chk = True if newleft_l < left_l else False
        if left_chk:
            left_l = newleft_l
            ret += 1
        left -= 1

    while right < n:
        newright_l = (li[right] - li[pos]) / (right - pos)
        right_chk = True if newright_l > right_l else False
        if right_chk:
            right_l = newright_l
            ret += 1
        right += 1
    return ret

answer = 0
for i in range(n):
    ans = solve(i)
    if answer < ans:
        answer = ans
print(answer)