n = int(input())
conn = int(input())

conn_lst = [list(map(int, input().split())) for _ in range(conn)]
v = [0] * (n+1)

def dfs(conn_lst, v, start):
    if v[start] == 1:
        pass
    else:
        v[start] = 1
        for i in conn_lst:
            if start == i[0]:
                dfs(conn_lst, v, i[1])
            elif start == i[1]:
                dfs(conn_lst, v, i[0])    

dfs(conn_lst, v, 1)

print(v.count(1) - 1)