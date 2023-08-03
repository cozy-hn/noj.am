ip=[*map(int,input().split())]
ip.pop()

def move(n,m):
    if n==m:
        return 1
    if n==0:
        return 2
    if abs(n-m)==2:
        return 4
    else:
        return 3

MAX=400000
N=len(ip)
if N==0:
    print(0)
    exit()
dp = [[[MAX for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(1,N+1):
    for r in range(5):
        for l in range(5):
            dp[i][r][ip[i-1]]=min(dp[i][r][ip[i-1]],dp[i-1][r][l]+move(l,ip[i-1]))
            dp[i][ip[i-1]][l]=min(dp[i][ip[i-1]][l],dp[i-1][r][l]+move(r,ip[i-1]))

print(min([min(dp[N][i]) for i in range(5)]))