n, s = map(int, input().split())
li = list(map(int, input().split()))
f_idx = 0
l_idx = -1
sm = 0
answer = 100001
while l_idx < n and f_idx < n:
    l_idx += 1
    if l_idx == n:
        l_idx = n-1
        while f_idx < n:
            sm -= li[f_idx]
            f_idx += 1
            if sm >= s and l_idx - f_idx + 1 < answer:
                answer = l_idx - f_idx + 1
        
        break
    else:
        sm += li[l_idx]
        re = 0
        while sm >= s and f_idx < l_idx:
            sm -= li[f_idx]
            f_idx += 1
            re = 1
        if re:
            f_idx -= 1
            sm += li[f_idx]
        
        if sm >= s and l_idx - f_idx + 1 < answer:
            answer = l_idx - f_idx + 1
if answer == 100001:
    answer = 0

print(answer)
    