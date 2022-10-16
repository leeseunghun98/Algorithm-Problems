n = int(input())
a, b = 1, 2
for i in range(n-2):
    b += a
    a = b - a
    b %= 15746
    a %= 15746
if n == 1:
    print(1)
else:
    print(b%15746)