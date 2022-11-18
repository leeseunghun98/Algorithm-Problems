import sys
input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    s, v = map(int, input().split())
    finish = v - s
    height = 1
    h_s = height*(height+1)
    while h_s < finish:
        height += 1
        h_s = height*(height+1)
    if h_s - height >= finish:
        print(2*height-1)
    else:
        print(2*height)