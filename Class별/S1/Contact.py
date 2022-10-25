import re
testcase = int(input())
ret = re.compile('(100+1+|01)+')
for _ in range(testcase):
    num = input()
    if ret.fullmatch(num): # match면 일부분이면 true반환
        print("YES")
    else:
        print("NO")