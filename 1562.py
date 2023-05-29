N=int(input())
MOD=10**9
dp=[0]+[1]*9
tmp=[0]*10
for _ in range(1,N):
    for i in range(10):
        tmp[i]=dp[i]
    for i in range(1,9):
        dp[i]=(tmp[i-1]+tmp[i+1])%MOD
    dp[0]=tmp[1]
    dp[9]=tmp[8]
print(sum(dp)%MOD)