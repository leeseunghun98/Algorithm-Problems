import sys
input = sys.stdin.readline
n = int(input())
MX = 1003001
che = [1 for _ in range(MX + 1)]
for i in range(2, (MX//2)+1):
    if che[i]:
        tmp =  2*i
        while tmp < MX + 1:
            che[tmp] = 0
            tmp += i
che[1] = 0
for i in range(n, MX + 1):
    if che[i] and str(i) == str(i)[::-1]:
        print(i)
        break