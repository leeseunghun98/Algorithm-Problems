import sys
input = sys.stdin.readline
n,m = map(int, input().split())
li = [i for i in range(n+1)]
dicts = {}
for i in range(n+1):
    dicts[i] = [i]
for _ in range(m):
    a, b, c = map(int, input().split())
    if a:
        print("YES" if li[b] == li[c] else "NO")
    else:
        if li[b] != li[c]:
            added = b if len(dicts.get(li[b], [])) >= len(dicts.get(li[c], [])) else c
            sub = b if added == c else c
            temp = li[sub]
            for i in dicts[li[sub]]:
                dicts[li[added]].append(i)
                li[i] = li[added]
            dicts[temp] = []