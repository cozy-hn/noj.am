import sys
input=lambda:sys.stdin.readline()

n=int(input())
Map=[list(map(int,input().split())) for _ in range(n)]
dp=[[0,0,0] for _ in range(n)]
dp[0]=Map[0]
for i in range(1,n):
    for j in range(3):
        dp[i][j]=min(dp[i-1][k] for k in range(3) if k!=j)+Map[i][j]
print(min(dp[-1]))