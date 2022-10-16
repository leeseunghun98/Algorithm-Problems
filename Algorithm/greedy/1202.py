import sys
N, K = map(int, sys.stdin.readline().split())
Ni = []
Ki = []
for _ in range(N):
    Ni.append(list(map(int, sys.stdin.readline().split())))
for _ in range(K):
    Ki.append(int(sys.stdin.readline()))
    
Ni.sort(key= lambda x:x[1], reverse=True)
Ki.sort()

result = 0
for n in Ni:
    if not Ki:
        break
    for idx, k in enumerate(Ki):
        if n[0] <= k:
            Ki.pop(idx)
            result += n[1]
            break
print(result)