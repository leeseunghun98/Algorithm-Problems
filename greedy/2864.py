A, B = map(list, input().split())

for idx, i in enumerate(A):
    if i == '5':
        A[idx] = '6'
for idx, i in enumerate(B):
    if i == '5':
        B[idx] = '6'
mx = int("".join(A)) + int("".join(B))
for idx, i in enumerate(A):
    if i == '6':
        A[idx] = '5'
for idx, i in enumerate(B):
    if i == '6':
        B[idx] = '5'
mn = int("".join(A)) + int("".join(B))
print(mn, mx)