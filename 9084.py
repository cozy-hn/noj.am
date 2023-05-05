import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    coin=list(map(int,input().split()))
    dp=[0]*(int(input())+1)
    dp[0]=1
    for i in coin:
        for j in range(i,len(dp)):
            dp[j]+=dp[j-i]
    print(dp[-1])