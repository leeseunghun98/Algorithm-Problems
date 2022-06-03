import sys
n = int(sys.stdin.readline())
li = set([])
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s == 'all':
        li = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif s == 'empty':
        li = set([])
    else:
        s, x = s.split()
        x = int(x)
        if s == 'add':
            li.add(x)
        elif s == 'remove':
            if x in li:
                li.remove(x)
        elif s == 'check':
            if x in li:
                print(1)
            else:
                print(0)
        else:
            if x in li:
                li.remove(x)
            else:
                li.add(x)