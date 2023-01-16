import sys
input = sys.stdin.readline
testcase = int(input())

def find(a):
    if a == parent_dic[a]:
        return a
    parent_dic[a] = find(parent_dic[a])
    return parent_dic[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent_dic[b] = a
        num[a] += num[b]

for _ in range(testcase):
    n = int(input())
    parent_dic = {}
    num = {}
    for _ in range(n):
        a, b = input().split()
        
        if a not in parent_dic:
            parent_dic[a] = a
            num[a] = 1
        if b not in parent_dic:
            parent_dic[b] = b
            num[b] = 1
        
        union(a, b)
        print(num[find(a)])