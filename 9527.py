from math import log2
A,B=map(int,input().split())
dp=[0]*int(log2(B)+1)
for i in range(1,len(dp)):
    dp[i]=dp[i-1]*2+2**(i-1)

def solve(N):
    if N<=0:
        return 0
    cut=int(log2(N))
    return dp[cut]+(N-2**cut+1)+solve(N-2**cut)

print(solve(B)-solve(A-1))
