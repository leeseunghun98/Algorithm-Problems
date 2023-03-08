import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
god = [tuple(map(int, input().split())) for _ in range(n)]
ways = [tuple(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x
    par = find(parent[x])
    parent[x] = par
    return par

def union(x, y):
    x_par = find(x)
    y_par = find(y)
    if x_par == y_par:
        return True
    if x_par < y_par:
        parent[y_par] = x_par
    else:
        parent[x_par] = y_par
    return False

def getDistance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

roads = []
for i in range(n):
    for j in range(i+1, n):
        roads.append((getDistance(god[i], god[j]), i+1, j+1))
roads.sort(key=lambda x:-x[0])

for i in ways:
    union(i[0], i[1])

answer = 0
while roads:
    dist, a, b = roads.pop()
    if union(a, b):
        continue
    answer += dist
print(format(answer,".2f"))