n = int(input("Enter the number: "))

total = [[0]*n for _ in range(n)]
k = 1

t,l,d,r = 0,0,n-1,n-1

while(k<=n*n):
    for i in range(t, d+1):
        total[l][i] = k
        k = k+1
    l = l+1
    for i in range(l, r+1):
        total[i][r] = k
        k = k+1
    d = d-1
    for i in range(d, t-1, -1):
        total[r][i] = k
        k = k+1
    r = r-1
    for i in range(r, l-1, -1):
        total[i][l-1] = k
        k = k+1
    t = t+1

for i in total:
    for j in i:
      if j <=9:
        print(j, end = '  ')
      else:
        print(j, end = ' ')
    print()
