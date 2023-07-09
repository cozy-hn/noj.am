N=int(input())
alen=int(input())
A=[*map(int,input().split())]
blen=int(input())
B=[*map(int,input().split())]

prefixA=[0]*(alen+1)
for i in range(alen):
    prefixA[i+1]=prefixA[i]+A[i]
prefixB=[0]*(blen+1)
for i in range(blen):
    prefixB[i+1]=prefixB[i]+B[i]

Adic={}
for i in range(1,alen+1):
    for j in range(i):
        tmp=prefixA[i]-prefixA[j]
        Adic[tmp]=Adic.get(tmp,0)+1
Bdic={}
for i in range(1,blen+1):
    for j in range(i):
        tmp=prefixB[i]-prefixB[j]
        Bdic[tmp]=Bdic.get(tmp,0)+1 

ans=0
PrefixA=list(Adic.keys())
PrefixB=list(Bdic.keys())
PrefixB.sort()
for i in PrefixA:
    if N-i in Bdic:
        ans+=Adic[i]*Bdic[N-i]
print(ans)