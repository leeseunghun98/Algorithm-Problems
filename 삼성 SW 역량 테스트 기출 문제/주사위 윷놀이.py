nums = tuple(map(int, input().split()))
dies = [[0, 0] for _ in range(4)]
lst0 = tuple(2*i for i in range(21)) # 21
lst1 = (10, 13, 16, 19, 25, 30, 35, 40) # 8
lst2 = (20, 22, 24, 25, 30, 35, 40) # 7
lst3 = (30, 28, 27, 26, 25, 30, 35, 40) # 8
li = (lst0, lst1, lst2, lst3)
len_list = (20, 7, 6, 7)
result = 0
answer = 0
def dfs(depth, livedi):
    global result
    global answer
    if depth == 10:
        if answer < result:
            answer = result
        return
    for i in livedi:
        cur = dies[i]
        next = cur[1] + nums[depth]
        if next > len_list[cur[0]]:
            index = livedi.index(i)
            livedi.pop(index)
            dfs(depth+1, livedi)
            livedi.insert(index, i)
        else:
            next_pos = [0, 0]
            if cur[0] == 0:
                if next == 5:
                    next_pos = [1, 0]
                elif next == 10:
                    next_pos = [2, 0]
                elif next == 15:
                    next_pos = [3, 0]
                else:
                    next_pos = [0, next]
            elif cur[0] == 1:
                next_pos = [1, next]
            elif cur[0] == 2:
                next_pos = [2, next]
            else:
                next_pos = [3, next]
            re = 0
            for live in livedi:
                if dies[live] == next_pos:
                    re = 1
                    break
            if re == 0:
                ans = li[next_pos[0]][next_pos[1]]
                result += ans
                dies[i] = next_pos
                dfs(depth+1, livedi)
                dies[i] = cur
                result -= ans

dfs(0, [0, 1, 2, 3])
print(answer)
