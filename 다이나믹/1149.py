import sys
N = int(sys.stdin.readline().rstrip('\n'))
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().rstrip('\n').split())))
result_li = [li[0]]
for i in range(1, N):
    lst = [li[i][0] + min(result_li[i-1][1], result_li[i-1][2]), 
           li[i][1] + min(result_li[i-1][0], result_li[i-1][2]), 
           li[i][2] + min(result_li[i-1][1], result_li[i-1][0])]
    result_li.append(lst)
print(min(result_li[-1]))