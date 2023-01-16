import sys
input = sys.stdin.readline
w, n = map(int, input().split())
li = [tuple(map(int, input().split())) for _ in range(n)]   
li.sort(key = lambda x:x[1])
answer = 0
while w > 0:
    if li:
        q, e = li.pop()
        w -= q
        answer += q * e
    else: break

print(answer + w * e)