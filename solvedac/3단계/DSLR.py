import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    A,B = map(int,input().split())
    queue = deque([(A,"")])
    visit = [0] * 10000
    while queue:
        num, path = queue.popleft()
        visit[num] = 1
        if num == B:
            print(path)
            break
        num2 = (2*num)%10000
        if not visit[num2]:
            queue.append((num2,path+"D"))
            visit[num2] = 1
        num2 = (num-1)%10000
        if not visit[num2]:
            queue.append((num2,path+"S"))
            visit[num2] = 1
        num2 = (10*num+(num//1000))%10000
        if not visit[num2]:
            queue.append((num2,path+"L"))
            visit[num2] = 1
        num2 = (num//10+(num%10)*1000)%10000
        if not visit[num2]:
            queue.append((num2,path+"R"))
            visit[num2] = 1