import sys
ipnut = sys.stdin.readline
n = int(input())
li = sorted(tuple(map(int, input().split())))
front = 0
back = n-1
answer = abs(li[front] + li[back])
answer_li = [li[front], li[back]]

while front < back:

    if abs(li[front] + li[back]) < answer:
        answer = abs(li[front] + li[back])
        answer_li[0] = li[front]
        answer_li[1] = li[back]
        if answer == 0:
            break
    
    if li[front] + li[back] > 0:
        back -= 1
    else:
        front += 1

print(*answer_li)