import sys
input = sys.stdin.readline
n, k = input().split()
if len(n) == 1 or (len(n) == 2 and n[1] == '0'):
    answer = [-1]
else:
    k = int(k)
    n = list(map(int, n))
    st = set(n)
    re = 0
    m = len(n)
    max_num = sorted(n, key=lambda x:-x)
    if len(st) != len(n):
        re = 1
    have_to_be_changed = -1
    answer = []
    for i in range(m):
        if n[i] != max_num[i]:
            have_to_be_changed = i
            break
    if have_to_be_changed == -1:
        if re:
            answer = max_num
        else:
            if k % 2:
                tmp = max_num[-2]
                max_num[-2] = max_num[-1]
                max_num[-1] = tmp
            answer = max_num
    else:
        for a in range(k):
            if have_to_be_changed >= m:
                if re:
                    answer = max_num
                else:
                    if (k - a) % 2:
                        tmp = max_num[-2]
                        max_num[-2] = max_num[-1]
                        max_num[-1] = tmp
                    answer = max_num
                break
            target = max_num[have_to_be_changed]
            for i in range(m-1, have_to_be_changed, -1):
                if target == n[i]:
                    n[i] = n[have_to_be_changed]
                    n[have_to_be_changed] = target
                    break
            while have_to_be_changed < m and n[have_to_be_changed] == max_num[have_to_be_changed]:
                have_to_be_changed += 1
            answer = n
print(''.join(map(str, answer)))