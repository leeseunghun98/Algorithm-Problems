import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = {}
    for i in range(n):
        _, b = sys.stdin.readline().rstrip().split()
        if b not in li:
            li[b] = 1
        else:
            li[b] += 1
    li = list(li.values())
    result = 1
    for i in li:
        result *= (i+1)
    print(result-1)