import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for i in range(1, n+1):
    dic[str(i)] = sys.stdin.readline().strip()
reverse_dic= dict(map(reversed, dic.items()))
Q = [sys.stdin.readline().strip() for _ in range(m)]
for i in Q:
    if i in dic:
        print(dic[i])
    else:
        print(reverse_dic[i])