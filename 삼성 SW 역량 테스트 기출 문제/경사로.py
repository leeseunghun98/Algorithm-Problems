N, L = map(int, input().split())
li = [tuple(map(int, input().split())) for _ in range(N)]

def find(lst, L):
    for i in range(1, len(lst)):
        if lst[i - 1] == lst[i] + 1:
            for j in range(L):
                if (0 <= i + j < len(lst)) and lst[i + j] == lst[i]:
                    visited[i + j] += 1
                    if visited[i + j] > 1:
                        return False
                else:
                    return False
        elif lst[i - 1] + 1 == lst[i]:
            for j in range(L):
                if (0 <= i - 1 - j < len(lst)) and lst[i - j - 1] == lst[i - 1]:
                    visited[i - 1 - j] += 1
                    if visited[i - 1 - j] > 1:
                        return False
                else:
                    return False
        elif lst[i - 1] > lst[i] or lst[i - 1] < lst[i]:
            return False
    return True
    
answer = 0
for i in li:
    visited = [0] * N
    if find(i, L):
        answer += 1

for i in range(N):
    a = []
    visited = [0] * N
    for j in range(N):
        a.append(li[j][i])
    if find(a, L):
        answer += 1

print(answer)