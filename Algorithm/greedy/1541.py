n = input()
a = n.split('-')

for idx, v in enumerate(a):
    a[idx] = sum(list(map(int, v.split('+'))))

print(a[0] - sum(a[1:]))