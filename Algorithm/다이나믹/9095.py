testcase = int(input())
li = [0] * 11
li[1] = 1
li[2] = 2
li[3] = 4
for i in range(4, 11):
    li[i] = li[i-1] + li[i-2] + li[i-3]
for _ in range(testcase):
    print(li[int(input())])