N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")
for x in range(N-2):
    for y in range(1, N-1):
        for d1 in range(1, min(y+1, N-1-x)):
            for d2 in range(1, min(N-y, N-x-d1)):
                peoples = [0, 0, 0, 0, 0]
                for r in range(N):
                    for c in range(N):
                        if c <= r-x+y and c >= x+y-r and c >= r-x+y-2*d1 and c <= x+y+2*d2-r:
                            peoples[4] += li[r][c]
                        elif r < x+d1 and c <= y:
                            peoples[0] += li[r][c]
                        elif r <= x+d2 and y < c:
                            peoples[1] += li[r][c]
                        elif x+d1 <= r and c < y-d1+d2:
                            peoples[2] += li[r][c]
                        elif x+d2 < r and y-d1+d2 <= c:
                            peoples[3] += li[r][c]
                        else:
                            peoples[4] += li[r][c]
                mx = max(peoples)
                mn = min(peoples)
                
                if answer > mx - mn:
                    answer = mx - mn
print(answer)