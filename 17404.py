import sys
input=lambda:sys.stdin.readline()

n=int(input())
Map=[list(map(int,input().split())) for _ in range(n)]
dp=[[0,0,0] for _ in range(n)]
tmp=Map[-1][:]
dp[1][0],Map[-1][0]=10**6,10**6
dp[1][1]=Map[1][1]+Map[0][0]
dp[1][2]=Map[1][2]+Map[0][0]
for i in range(2,n):
    for j in range(3):
        dp[i][j]=min(dp[i-1][k] for k in range(3) if k!=j)+Map[i][j]
# print(dp)
st1=min(dp[-1])

dp=[[0,0,0] for _ in range(n)]
Map[-1]=tmp[:]
dp[1][1]=10**6
Map[-1][1]=10**6
dp[1][0]=Map[1][0]+Map[0][1]
dp[1][2]=Map[1][2]+Map[0][1]
for i in range(2,n):
    for j in range(3):
        dp[i][j]=min(dp[i-1][k] for k in range(3) if k!=j)+Map[i][j]
# print(dp)
st2=min(dp[-1])

dp=[[0,0,0] for _ in range(n)]
Map[-1]=tmp[:]
Map[-1][2],dp[1][2]=10**6,10**6
dp[1][1]=Map[1][1]+Map[0][2]
dp[1][0]=Map[1][0]+Map[0][2]
for i in range(2,n):
    for j in range(3):
        dp[i][j]=min(dp[i-1][k] for k in range(3) if k!=j)+Map[i][j]
# print(dp)
st3=min(dp[-1])

print(min(st1,st2,st3))