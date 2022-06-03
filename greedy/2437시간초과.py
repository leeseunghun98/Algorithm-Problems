N = int(input())
li = list(map(int, input().split()))
li.sort()
n = 1
pregap = 0
while True:
    bin = format(n, 'b')[::-1]
    gap = 0
    for idx, i in enumerate(bin):
        if i == '1':
            gap += li[idx]
    
    if gap > pregap + 1:
        print(pregap + 1)
        break
    if gap >= pregap:
        pregap = gap
    n += 1