from collections import Counter
N,M=map(int,input().split())
li=[*map(int,input().split())]
SUM=[0]*(N+1)
for i in range(1,N+1):
    SUM[i]=SUM[i-1]+li[i-1]
MOD=[i%M for i in SUM]
DIC=Counter(MOD)
MODNUM=[DIC.get(i,0) for i in range(M)]
ans=0
for i in range(1,len(MODNUM)):
    ans+=MODNUM[i]*(MODNUM[i]-1)//2
ans+=(MODNUM[0]-1)*(MODNUM[0]-2)//2
print(ans+MODNUM[0]-1)