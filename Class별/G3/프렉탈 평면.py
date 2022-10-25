time, n, k, r1, r2, c1, c2 = map(int, input().split())
li = [[0]]

for _ in range(time):
    lst = []
    for i in li:
        l = [[] for _ in range(n)]
        for j in i:
            if j: # 검정
                for q in range(n):
                    l[q] += [1] * n
            else: # 흰색
                a = (n - k) // 2
                for q in range(a):
                    l[q] += [0] * n
                for q in range(a, a+k):
                    l[q] += [0] * a + [1] * k + [0] * a
                for q in range(a+k, n):
                    l[q] += [0] * n

        lst += l
    li = lst

for i in range(r1, r2+1):
    print(*li[i][c1:c2+1], sep="")