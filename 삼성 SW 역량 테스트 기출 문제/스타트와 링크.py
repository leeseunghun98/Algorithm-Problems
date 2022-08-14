from itertools import combinations

N = int(input())
li = [tuple(map(int, input().split())) for _ in range(N)]
                
def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:], r-1):
                yield [array[i]] + next
                
r = N // 2
lst = [i for i in range(N)]
lst_set = set(lst)
result = float("inf")
for i in combinations(lst, r):
    a = i
    i = set(i)
    b = list(lst_set - i)
    a_result = 0
    b_result = 0
    for j in combinations(a, 2):
        a_result += (li[j[0]][j[1]] + li[j[1]][j[0]])
    for j in combinations(b, 2):
        b_result += (li[j[0]][j[1]] + li[j[1]][j[0]])
    if abs(b_result - a_result) < result:
        result = abs(b_result - a_result)
print(result)
