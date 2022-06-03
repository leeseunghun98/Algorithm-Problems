n = int(input())
li = [[0] for _ in range(100)]
li[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(99):
    li[i+1] = [li[i][1], li[i][0]+li[i][2], li[i][1]+li[i][3], li[i][2]+li[i][4], 
             li[i][3]+li[i][5], li[i][4]+li[i][6], li[i][5]+li[i][7], li[i][6]+li[i][8], 
             li[i][7]+li[i][9], li[i][8]]
print(sum(li[n-1])%1000000000)