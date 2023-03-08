import sys
input = sys.stdin.readline
li = [list(map(int, input().split())) for _ in range(10)]
boundary = lambda x, y: True if x < 10 and y < 10 else False
ones = 0
for i in range(10):
    for j in range(10):
        if li[i][j] == 1:
            ones += 1

# def isSquare(x, y, l):



# def dfs(l, num):
#     if num == ones:
#         return True
#     if l == 0:
#         return False
    
#     for i in range(11-l):
#         for j in range(11-l):
#             isSquare(i, j, l)