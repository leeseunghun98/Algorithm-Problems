n = input().rstrip()

answer = [0 for _ in range(10)]
before = 0
after = n[1:]
len_ = len(n)-1
for i in range(len(n)):
    if i > 0:
        answer[0] += (before-1) * (10 ** (len_ - i))
    for j in range(1, 10):
        answer[j] += before * (10 ** (len_ - i))
    start = i == 0
    for j in range(start, int(n[i])):
        answer[j] += 10 ** (len_ - i)
    if after:
        answer[int(n[i])] += (int(after) + 1)
    else:
        answer[int(n[i])] += 1
    before = before * 10 + int(n[i])
    after = after[1:]

print(*answer)