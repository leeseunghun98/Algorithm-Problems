li = tuple(map(int, input().split()))
roads = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
         [10, 13, 16, 19],
         [20, 22, 24],
         [30, 28, 27, 26],
         [25, 30, 35], 
         [40]]
nextStage = [5, 4, 4, 4, 5, 6]

answer = 0

def checkAlready(positions, pos):
    if pos not in positions:
        return True
    return False

def dfs(positions, depth, score, inned):
    global answer
    if depth == 10:
        if answer < score:
            answer = score
        return
    
    if inned < 4:
        if li[depth] == 5:
            if checkAlready(positions, [1, 0]):
                dfs(positions + [[1, 0]], depth + 1, score + roads[1][0], inned + 1)
        else:
            if checkAlready(positions, [0, li[depth]]):
                dfs(positions + [[0, li[depth]]], depth + 1, score + roads[0][li[depth]], inned + 1)

    for i, p in enumerate(positions):
        onStage = p[0]
        go = p[1] + li[depth]
        while onStage < 6 and go >= len(roads[onStage]):
            go -= len(roads[onStage])
            onStage = nextStage[onStage]
        dest = [onStage, go]
        if dest[0] == 0 and dest[1] % 5 == 0:
            dest[0] = dest[1] // 5
            dest[1] = 0
        if checkAlready(positions, dest):
            if dest[0] == 6:
                re = positions.pop(i)
                dfs(positions, depth + 1, score, inned)
                positions.insert(i, re)
            else:
                positions[i] = dest
                dfs(positions, depth + 1, score + roads[dest[0]][dest[1]], inned)
                positions[i] = p

dfs([], 0, 0, 0)
print(answer)