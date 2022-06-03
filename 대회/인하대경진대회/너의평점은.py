import sys
sub = [list(sys.stdin.readline().strip().split()) for _ in range(20)]
sub_down = 0
sub_up = 0
scores = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0}
for i in sub:
    if i[-1] != 'P':
        sub_down += float(i[1])
        sub_up += float(i[1]) * scores[i[2]]
print(format(sub_up/sub_down, ".6f"))