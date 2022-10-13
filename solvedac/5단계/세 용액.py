import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
answer = float("INF")
ans = []
for i in range(len(li)):
    start = i+1
    finish = len(li)-1
    if start == finish:
        break
    while finish > start:
        a = abs(li[finish] + li[start] + li[i])
        if answer > a:
            answer = a
            ans = [li[i], li[start], li[finish]]
        if li[finish] + li[start] + li[i] >= 0:
            finish -= 1
        else:
            start += 1
print(*ans)