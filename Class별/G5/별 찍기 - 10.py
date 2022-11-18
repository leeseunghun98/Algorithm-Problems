n = int(input())
li = ['*']
def square(d):
    if d == 1:
        return
    l = len(li)
    for i in range(l):
        li.append(li[i])
        li[-1] += ' ' * l
        li[-1] += li[i]
    for i in range(l):
        li.append(li[i] * 3)
    for i in range(l):
        li[i] += li[i]*2

    square(d//3)

square(n)
for i in li:
    print(i)