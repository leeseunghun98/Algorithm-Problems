import sys
input = sys.stdin.readline
l1 = tuple(map(int, input().split()))
l1 = sorted([(l1[0], l1[1]), (l1[2], l1[3])])
x1, y1 = l1[0]; x2, y2 = l1[1]

l2 = tuple(map(int, input().split()))
l2 = sorted([(l2[0], l2[1]), (l2[2], l2[3])])
a1, b1 = l2[0]; a2, b2 = l2[1]

line1 = (y2-y1)/(x2-x1)
line2 = (b2-b1)/(a2-a1)
if line1 == line2:
    if y1==int(line2*x1+b1-line2*a1):
        print(1 if (a1<=x1<=a2) or (a1<=x2<=a2) else 0)
    else:
        print(0)
else:
    cross_x = int((b1-a1*line2-y1+x1*line1)/(line1-line2))
    print(1 if (a1<=cross_x<=a2) and (x1<=cross_x<=x2) else 0)