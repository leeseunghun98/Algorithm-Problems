import sys
input = sys.stdin.readline
n, k = map(int, input().split())
li = tuple((set(input().rstrip()[4:-4]) - {'a', 'n', 't', 'i', 'c'}) for _ in range(n))

answer = 0
if k < 5:
    answer = 0
else:
    for i in li:
        if len(i) <= k - 5:
            
            for j in li:


print(answer)

