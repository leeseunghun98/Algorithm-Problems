N = int(input())
li = list(map(int, input().split()))
li.sort()
if li[0] != 1:
    print(1)
else:
    for idx, i in enumerate(li):
        if idx == 0:
            continue
        if i > sum(li[:idx]) + 1:
            print(sum(li[:idx])+1)
            break
        elif idx == N-1:
            print(sum(li)+1)