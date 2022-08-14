# n = int(input())
# for i in range(11):
#     if 3 * (2 ** i) == n:
#         k = i
# total = 5
# center = 3 * (2 ** k) - 1
# for i in range(k):
#     total = total * 2 + 1
# li = [[' ' for _ in range(total)],[' ' for _ in range(total)],[' ' for _ in range(total)]]
# li[0][center] = '*'
# li[1][center-1], li[1][center+1] = "*", "*"
# li[2][center-2:center+2] = ["*", "*", "*", "*", "*"]

# for i in range(k):
#     len_ = len(li)
#     for j in range(len_):
#         a = [' ' for _ in range(total)]
#         for idx, q in enumerate(li[j]):
#             if q == '*':
#                 a[idx + 3*(2**i)] = '*'
#                 a[idx - 3*(2**i)] = '*'
#         li.append(a)

# for i in li:
#     print("".join(i))


n = int(input())

graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]


def recursive(N, before):
    after = [[" "] * (2 * 2 * N - 1) for _ in range(2 * N)]
    for i in range(N):
        after[i][N:N+2*N-1] = before[i]

    k = 0
    for i in range(N, 2 * N):
        after[i][:2*N] = before[k]
        after[i][2 * N:2 * N+len(before[k])] = before[k]
        k += 1

    if 2 * N == n:
        return after

    return recursive(2 * N, after)


if n == 3:
    result = graph
else:
    result = recursive(3, graph)

for i in result:
    print("".join(i))