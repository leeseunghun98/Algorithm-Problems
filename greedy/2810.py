N = int(input())
seat = list(input())
cups = [0] * (N+1)
L_count = 0
for i in range(N):
    if seat[i] == 'S':
        if cups[i] == 0:
            cups[i] = 1
        elif cups[i+1] == 0:
            cups[i+1] = 1
    else:
        L_count += 1
        if L_count % 2 == 1:
            if cups[i] == 0:
                cups[i] = 1
        elif cups[i+1] == 0:
            cups[i+1] = 1
print(sum(cups))