import sys
n, r, c = map(int, sys.stdin.readline().strip().split())
li = [2**14, 2**13, 2**12, 2**11, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
result = 0
while r > 0 or c > 0:
    for i in li:
        if r >= i and c >= i:
            r -= i
            c -= i
            result += 3 * (i ** 2)
            break
        elif r >= i:
            r -= i
            result += 2 * (i ** 2)
            break
        elif c >= i:
            c -= i
            result += i ** 2
            break
print(result)