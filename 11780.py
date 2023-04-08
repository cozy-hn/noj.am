n=int(input())
m=int(input())
INF=10**8
city=[[(INF,[])]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    if city[a-1][b-1][0]>c:
        city[a-1][b-1]=(c,[a])
for i in range(n):
    city[i][i]=(0,[])            
for k in range(n):
    for i in range(n):
        for j in range(n):
            if city[i][j][0]>city[i][k][0]+city[k][j][0]:
                city[i][j]=(city[i][k][0]+city[k][j][0],city[i][k][1]+city[k][j][1])
for i in range(n):
    for j in range(n):
        if city[i][j][0]==INF:
            city[i][j]=(0,[])
for i in range(n):
    for j in range(n-1):
        print(city[i][j][0],end=' ')
    print(city[i][n-1][0])
for i in range(n):
    for j in range(n):
        if city[i][j][1]:
            print(len(city[i][j][1])+1,*city[i][j][1],j+1)
        else:
            print('0')