import sys
input=lambda:sys.stdin.readline()

n=int(input())
Map=[list(map(int,input().split())) for _ in range(n)]
for i in range(1,n):
    for j in range(len(Map[i])):
        if j==0:
            Map[i][j]+=Map[i-1][j]
        elif j==len(Map[i])-1:
            Map[i][j]+=Map[i-1][j-1]
        else:
            Map[i][j]=max(Map[i-1][j],Map[i-1][j-1])+Map[i][j]
print(max(Map[-1]))