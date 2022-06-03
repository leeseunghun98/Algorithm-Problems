num = list(input())
cnt = 0

if num[0] == num[-1]:
    for i in range(len(num)-1):
        if num[i] == num[0] and num[i+1] == str((1 - int(num[0]))):
            cnt += 1
else:
    for i in range(len(num)-1):
        if num[i] == num[0] and num[i+1] == num[-1]:
            cnt += 1

print(cnt)