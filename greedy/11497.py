import sys
testcase = int(sys.stdin.readline().rstrip('\n'))
for _ in range(testcase):
    n = int(sys.stdin.readline().rstrip('\n'))
    li = list(map(int, sys.stdin.readline().rstrip('\n').split()))
    li.sort()
    lst = []
    idx = n-2
    gap = 0
    for i in range(0, n, 2):
        lst.append(li[i])
        if i == n-2:
            lst.append(li[n-1])
            idx = n-3
    for i in range(idx, 0, -2):
        lst.append(li[i])
    for i in range(-1, len(lst)-1):
        if lst[i]-lst[i+1] < 0:
            ga = -(lst[i]-lst[i+1])
        else:
            ga = lst[i]-lst[i+1]
        gap = max(ga, gap)
    print(gap)