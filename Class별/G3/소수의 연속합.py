n = int(input())
if n == 1:
    print(0)
    exit()
li = [True for _ in range(n+1)]
li[1] = False
for i in range(2, n+1):
    if li[i]:
        start = i * 2
        while start < n+1:
            li[start] = False
            start += i
che = []
for i in range(1, n+1):
    if li[i]:
        che.append(i)

left = 0
right = 0
sm = che[0]
answer = 0
while left < len(che):
    if right == len(che)-1:
        if sm == n:
            answer += 1
            break
        elif sm > n:
            sm -= che[left]
            left += 1
            continue
        break
    if sm == n:
        answer += 1
        right += 1
        sm += che[right]
    elif sm > n:
        sm -= che[left]
        left += 1
    else:
        right += 1
        sm += che[right]

print(answer)