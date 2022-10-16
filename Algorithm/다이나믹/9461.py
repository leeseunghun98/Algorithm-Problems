testcase = int(input())
li = [0] * 100
li[0], li[1], li[2] = 1, 1, 1
li[3], li[4] = 2, 2
li[5] = 3
for i in range(6, 100):
    li[i] = li[i-5] + li[i-1]
for _ in range(testcase):
    print(li[int(input())-1])