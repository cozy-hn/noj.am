N=int(input())
li=list(map(int,input().split()))
dp=[10**6]*(N+1)
if N>=1:
    dp[1]=li[0]*3
if N>=2:
    dp[2]=min(dp[0]+li[1]*3,min(li[0],li[1])*5+abs(li[0]-li[1])*3)
if N>=3:
    dp[0]=0
    for i in range(2,N):
        tmp=min(li[i-2],li[i-1],li[i])
        if tmp==li[i-2]:
            if li[i-1]>li[i] and i!=N-1 and li[i+1]>0:
                if li[i-2]<=li[i-1]-li[i]:
                    tmp=li[i-2]*5+min(li[i-1]-li[i-2],li[i])*5+abs(li[i-1]-li[i-2]-li[i])*3
                else:
                    tmp=(li[i-1]-li[i])*5+(li[i-2]-li[i-1]+li[i])*7+(li[i]-li[i-2])*5
            else:
                tmp=li[i-2]*7+(min(li[i-1],li[i])-li[i-2])*5+abs(li[i-1]-li[i])*3
        elif tmp==li[i-1]:
            tmp=li[i-1]*7+li[i-2]*3+li[i]*3
        else:
            if li[i-1]>li[i] and i!=N-1 and li[i+1]>0:
                if li[i-2]<=li[i-1]-li[i]:
                    tmp=li[i-2]*5+min(li[i-1]-li[i-2],li[i])*5+abs(li[i-1]-li[i-2]-li[i])*3
                else:
                    tmp=(li[i-1]-li[i])*5+(li[i-2]-li[i-1]+li[i])*7+(li[i]-li[i-2])*5
            else:
                tmp=li[i]*7+(min(li[i-1],li[i-2])-li[i])*5+abs(li[i-1]-li[i-2])*3
        dp[i+1]=min(dp[i]+li[i]*3,dp[i-1]+min(li[i-1],li[i])*5+abs(li[i-1]-li[i])*3,dp[i-2]+tmp)
# print(dp)
# print(li)
print(dp[-1])