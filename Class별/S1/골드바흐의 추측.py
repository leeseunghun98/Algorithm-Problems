import sys
from bisect import bisect_left
input = sys.stdin.readline
MX = 1000001

che = [True for _ in range(MX)]
che[1] = False
primes = []
for i in range(2, MX):
    if che[i]:
        primes.append(i)
        next = i * 2
        while next < MX:
            che[next] = False
            next += i
che[2] = False
primes = primes[1:]

while True:
    n = int(input())
    if n == 0:
        break

    end = bisect_left(primes, n)
    if end == len(primes):
        end -= 1
    if primes[end] >= n:
        end -= 1
    target = n - primes[end]
    start = bisect_left(primes, target)
    
    while primes[start] != target and start <= end:
        end -= 1
        target = n - primes[end]
        start = bisect_left(primes, target)

    if primes[start] == target:
        print(n, '=', primes[start], '+', primes[end])
    else:
        print("Goldbach's conjecture is wrong.")