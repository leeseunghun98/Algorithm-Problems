n = int(input())
m = 1000000
fibonachi = [0, 1]
p = 15 * m // 10
for i in range(2, p):
    fibonachi.append((fibonachi[i-1] + fibonachi[i-2])%m)
print(fibonachi[n%p])