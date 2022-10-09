import sys
# 산 양수, 알칼리 음수
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
first = 0
last = n-1
answer = float("INF")

def chk(answer, c):
    chk2 = False
    if answer > abs(li[first] + li[last] + li[c]):
        answer = abs(li[first] + li[last] + li[c])
        chk2 = True
    if li[first] + li[last] >= 0:
        return [answer, True, chk2]
    else:
        return [answer, False, chk2]

def binary_search(first, last, target):
    tmp = first
    mid = (last + first) // 2
    ans = last
    while first <= last:
        if li[mid] >= target:
            last = mid - 1
            ans = mid
            mid = (last + first) // 2
        else:
            first = mid + 1
            mid = (last + first) // 2
    if ans == tmp:
        return ans + 1
    return ans

ans = []
while first + 1 < last:
    b = binary_search(first, last, -(li[first] + li[last]))
    a = b-1
    if a == first:
        if b != last:
            answer, check, chk2 = chk(answer, b)
            if chk2:
                ans = [li[first], li[b], li[last]]
        else:
            break
    else:
        if b == last:
            answer, check, chk2 = chk(answer, a)
            if chk2:
                ans = [li[first], li[a], li[last]]
        else:
            if abs(li[first] + li[last] + li[a]) < abs(li[first] + li[last] + li[b]):
                answer, check, chk2 = chk(answer, a)
                if chk2:
                    ans = [li[first], li[a], li[last]]
            else:
                answer, check, chk2 = chk(answer, b)
                if chk2:
                    ans = [li[first], li[b], li[last]]
    
    if check:
        last -= 1
    else:
        first += 1

print(*ans)
