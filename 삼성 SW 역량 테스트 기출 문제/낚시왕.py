R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
li = [[[[], []] for _ in range(C)] for _ in range(R)]
for idx, shark in enumerate(sharks):
    li[shark[0]-1][shark[1]-1] = [shark[2:], []]

dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, 1, -1)

def shark_move():
    for r in range(R):
        for c in range(C):
            if li[r][c][0]:
                dir = li[r][c][0][1]
                velocity = li[r][c][0][0]
                if dir == 1:
                    if r < velocity:
                        velocity -= r
                        left = (velocity // (R - 1)) % 2
                        left_ = velocity % (R - 1)
                        if left:
                            if (not li[R - 1 - left_][c][1]) or li[R - 1 - left_][c][1][2] < li[r][c][0][2]:
                                li[R - 1 - left_][c][1] = [li[r][c][0][0], 1, li[r][c][0][2]]
                        else:
                            if (not li[left_][c][1]) or li[left_][c][1][2] < li[r][c][0][2]:
                                li[left_][c][1] = [li[r][c][0][0], 2, li[r][c][0][2]]
                    else:
                        if (not li[r + velocity * dx[dir]][c + velocity * dy[dir]][1]) or li[r + velocity * dx[dir]][c + velocity * dy[dir]][1][2] < li[r][c][0][2]:
                            li[r + velocity * dx[dir]][c + velocity * dy[dir]][1] = [li[r][c][0][0], 1, li[r][c][0][2]]

                elif dir == 2:
                    if R - 1 - r < velocity:
                        velocity -= (R - 1 - r)
                        left = (velocity // (R - 1)) % 2
                        left_ = velocity % (R - 1)
                        if left:
                            if (not li[left_][c][1]) or li[left_][c][1][2] < li[r][c][0][2]:
                                li[left_][c][1] = [li[r][c][0][0], 2, li[r][c][0][2]]
                        else:
                            if (not li[R - 1 - left_][c][1]) or li[R - 1 - left_][c][1][2] < li[r][c][0][2]:
                                li[R - 1 - left_][c][1] = [li[r][c][0][0], 1, li[r][c][0][2]]
                    else:
                        if (not li[r + velocity * dx[dir]][c + velocity * dy[dir]][1]) or li[r + velocity * dx[dir]][c + velocity * dy[dir]][1][2] < li[r][c][0][2]:
                            li[r + velocity * dx[dir]][c + velocity * dy[dir]][1] = [li[r][c][0][0], 2, li[r][c][0][2]]

                elif dir == 3:
                    if C - 1 - c < velocity:
                        velocity -= (C - 1 - c)
                        left = (velocity // (C - 1)) % 2
                        left_ = velocity % (C - 1)
                        if left:
                            if (not li[r][left_][1]) or li[r][left_][1][2] < li[r][c][0][2]:
                                li[r][left_][1] = [li[r][c][0][0], 3, li[r][c][0][2]]
                        else:
                            if (not li[r][C - 1 - left_][1]) or li[r][C - 1 - left_][1][2] < li[r][c][0][2]:
                                li[r][C - 1 - left_][1] = [li[r][c][0][0], 4, li[r][c][0][2]]
                    else:
                        if (not li[r + velocity * dx[dir]][c + velocity * dy[dir]][1]) or li[r + velocity * dx[dir]][c + velocity * dy[dir]][1][2] < li[r][c][0][2]:
                            li[r + velocity * dx[dir]][c + velocity * dy[dir]][1] = [li[r][c][0][0], 3, li[r][c][0][2]]

                else:
                    if c < velocity:
                        velocity -= c
                        left = (velocity // (C - 1)) % 2
                        left_ = velocity % (C - 1)
                        if left:
                            if (not li[r][C - 1 - left_][1]) or li[r][C - 1 - left_][1][2] < li[r][c][0][2]:
                                li[r][C - 1 - left_][1] = [li[r][c][0][0], 4, li[r][c][0][2]]
                        else:
                            if (not li[r][left_][1]) or li[r][left_][1][2] < li[r][c][0][2]:
                                li[r][left_][1] = [li[r][c][0][0], 3, li[r][c][0][2]]
                    else:
                        if (not li[r + velocity * dx[dir]][c + velocity * dy[dir]][1]) or li[r + velocity * dx[dir]][c + velocity * dy[dir]][1][2] < li[r][c][0][2]:
                            li[r + velocity * dx[dir]][c + velocity * dy[dir]][1] = [li[r][c][0][0], 4, li[r][c][0][2]]
                li[r][c][0] = []
                
    for r in range(R):
        for c in range(C):
            if li[r][c][1]:
                li[r][c][0] = li[r][c][1]
                li[r][c][1] = []

answer = 0
for fisher_position in range(C):
    for shark in range(R):
        if li[shark][fisher_position][0]:
            answer += li[shark][fisher_position][0][2]
            li[shark][fisher_position][0] = []
            break
    shark_move()

print(answer)