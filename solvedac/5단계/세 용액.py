import sys

def solve():
    answer = float("INF")
    if li[0] > 0:
        print(*li[:3])
    elif li[-1] < 0:
        print(*li[-3:])
    else:
        for i in range(n-2):
            start = i+1
            finish = n-1
            while finish > start:
                q = li[finish] + li[start] + li[i]
                a = abs(q)
                if answer > a:
                    answer = a
                    ans = [li[i], li[start], li[finish]]
                if q > 0:
                    finish -= 1
                elif q < 0:
                    start += 1
                else:
                    break
            if sum(ans) == 0:
                break
        print(*ans)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    li = sorted(list(map(int, sys.stdin.readline().split())))
    solve()