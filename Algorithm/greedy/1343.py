test = list(input())
for i in range(len(test)):
    if i < len(test) - 3 and test[i] == 'X' and test[i+1] == 'X' and test[i+2] == 'X' and test[i+3] == 'X':
        test[i], test[i+1], test[i+2], test[i+3] = 'A', 'A', 'A', 'A'
    elif i < len(test) - 1 and test[i] == 'X' and test[i+1] == 'X':
        test[i], test[i+1] = 'B', 'B'
x = str(test).find('X')
if x != -1:
    print(-1)
else:
    print("".join(test))