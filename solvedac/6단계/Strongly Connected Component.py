import sys
input = sys.stdin.readline
v, e = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(e)]
vertex_visited = [0 for _ in range(v+1)]
line_visited = [0 for _ in range(e+1)]


