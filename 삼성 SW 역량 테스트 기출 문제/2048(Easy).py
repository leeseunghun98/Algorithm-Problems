import copy
def up(lst):
    li = [[i, 0] for i in lst[0]]
    mx = 0
    for i in range(1, n):
        for j in range(n):
            if lst[i][j] > 0:
                if li[j][0] == 0:
                    li[j][0] = lst[i][j]
                    lst[li[j][1]][j] = lst[i][j]
                    lst[i][j] = 0
                elif li[j][0] == lst[i][j]:
                    lst[li[j][1]][j] = 2 * li[j][0]
                    lst[i][j] = 0
                    li[j][1] += 1
                    li[j][0] = 0
                elif i - li[j][1] == 1:
                    li[j] = [lst[i][j], i]
                else:
                    li[j] = [lst[i][j], li[j][1] + 1]
                    lst[li[j][1]][j] = lst[i][j]
                    lst[i][j] = 0
            if mx < li[j][0]:
                mx = li[j][0]
    return mx

def down(lst):
    mx = 0
    li = [[i, n-1] for i in lst[-1]]
    for i in range(n-2, -1, -1):
        for j in range(n):
            if lst[i][j] > 0:
                if li[j][0] == 0:
                    li[j][0] = lst[i][j]
                    lst[li[j][1]][j] = lst[i][j]
                    lst[i][j] = 0
                elif li[j][0] == lst[i][j]:
                    lst[li[j][1]][j] = 2 * li[j][0]
                    lst[i][j] = 0
                    li[j][1] -= 1
                    li[j][0] = 0
                elif li[j][1] - i == 1:
                    li[j] = [lst[i][j], i]
                else:
                    li[j] = [lst[i][j], li[j][1] - 1]
                    lst[li[j][1]][j] = lst[i][j]
                    lst[i][j] = 0
            if mx < li[j][0]:
                mx = li[j][0]
    return mx

def left(lst):
    li = [[i[0], 0] for i in lst]
    mx = 0
    for j in range(1, n):
        for i in range(n):
            if lst[i][j] > 0:
                if li[i][0] == 0:
                    lst[i][li[i][1]] = lst[i][j]
                    li[i][0] = lst[i][j]
                    lst[i][j] = 0
                elif li[i][0] == lst[i][j]:
                    lst[i][li[i][1]] = 2 * li[i][0]
                    lst[i][j] = 0
                    li[i][1] += 1
                    li[i][0] = 0
                elif j - li[i][1] == 1:
                    li[i] = [lst[i][j], j]
                else:
                    li[i] = [lst[i][j], li[i][1] + 1]
                    lst[i][li[i][1]] = lst[i][j]
                    lst[i][j] = 0
            if mx < li[i][0]:
                mx = li[i][0]
    return mx

def right(lst):
    li = [[i[-1], n-1] for i in lst]
    mx = 0
    for j in range(n-2, -1, -1):
        for i in range(n):
            if lst[i][j] > 0:
                if li[i][0] == 0:
                    lst[i][li[i][1]] = lst[i][j]
                    li[i][0] = lst[i][j]
                    lst[i][j] = 0
                elif li[i][0] == lst[i][j]:
                    lst[i][li[i][1]] = 2 * li[i][0]
                    lst[i][j] = 0
                    li[i][1] -= 1
                    li[i][0] = 0
                elif li[i][1] - j == 1:
                    li[i] = [lst[i][j], j]
                else:
                    li[i] = [lst[i][j], li[i][1] - 1]
                    lst[i][li[i][1]] = lst[i][j]
                    lst[i][j] = 0
            if mx < li[i][0]:
                mx = li[i][0]
    return mx

def solution(lst, depth):
    if depth == 6:
        return
    global answer
    li = copy.deepcopy(lst)
    res = up(li)
    solution(li, depth+1)
    if answer < res:
        answer = res
    
    li = copy.deepcopy(lst)
    res = down(li)
    solution(li, depth+1)
    if answer < res:
        answer = res
    
    li = copy.deepcopy(lst)
    res = left(li)
    solution(li, depth+1)
    if answer < res:
        answer = res
    
    li = copy.deepcopy(lst)
    res = right(li)
    solution(li, depth+1)
    if answer < res:
        answer = res

n = int(input())
if n == 1:
    print(int(input()))
else:
    li = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    solution(li, 0)
    print(answer)