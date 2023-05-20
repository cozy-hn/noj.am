N,S=map(int,input().split())
ip=[0]+list(map(int,input().split()))
prefixsum=[0]*(N+1)
p1,p2=0,1
ans=10**9+1
for i in range(1,len(prefixsum)):
    prefixsum[i]=prefixsum[i-1]+ip[i]
while p1<=p2 and p2<len(prefixsum):
    if prefixsum[p2]-prefixsum[p1]>=S:
        ans=min(ans,p2-p1)
        p1+=1
    else:
        p2+=1
print(ans if ans!=10**9+1 else 0)