import sys
input = sys.stdin.readline
len_li, k = map(int, input().strip().split())
li = list(input().strip())
visited = [0] * len_li
result = 0
for i in range(len_li):
    for j in range(-k, k+1):
        if (0<=i+j<len_li)and li[i] == 'P' and li[i+j] == 'H' and visited[i+j] == 0:
            visited[i+j] = 1
            result += 1
            break
print(result)