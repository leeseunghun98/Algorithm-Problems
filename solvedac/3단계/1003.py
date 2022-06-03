import sys
li = [0] * 41
li[0] = [1, 0]
li[1] = [0, 1]
for i in range(2, 41):
    li[i] = [li[i-1][0] + li[i-2][0], li[i-1][1] + li[i-2][1]]
for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    print(li[n][0], li[n][1])