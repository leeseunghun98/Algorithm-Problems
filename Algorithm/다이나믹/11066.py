import sys
input = sys.stdin.readline
testcase = int(input().strip())
for _ in range(testcase):
    k = int(input().strip())
    li = list(map(int, input().strip().split()))
    li.sort()
    result = 0
    for q in range(k-1):
        a = li.pop(0)
        b = li.pop(0)
        c = a + b
        idx = 0
        while idx < k - q - 2 and c > li[idx]:
            idx += 1
        li.insert(idx, c)
        result += c
        print(c)
    print(result)