s1=input()
s2=input()

def LCS(s1,s2):
    dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1], getLCS(dp,s1,s2)

def getLCS(dp,s1,s2):
    rtn=[]
    i,j=len(s1),len(s2)
    while i>0 and j>0:
        if dp[i][j]==dp[i-1][j]: i-=1
        elif dp[i][j]==dp[i][j-1]: j-=1
        else:
            rtn.append(s1[i-1])
            i-=1
            j-=1
    return rtn[::-1]

ans,ansli=LCS(s1,s2)
print(ans)
print(*ansli,sep="")