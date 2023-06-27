N,S=map(int,input().split())
seq=[*map(int,input().split())]
lrans=0
lSlist,rSlist=[],[]

def solve(l,r,Slist):
    global lrans
    slen=0
    for i in range(l,r):
        tslen=slen
        for j in range(tslen):
            tmp=Slist[j]+seq[i]
            Slist.append(tmp)
            if tmp==S:
                lrans+=1
        Slist.append(seq[i])
        if seq[i]==S:
            lrans+=1
        slen+=tslen+1
    return slen

llen=solve(0,N//2,lSlist)
rlen=solve(N//2,N,rSlist)
lSlist.sort()
rSlist.sort()
both=0
lidx,ridx=0,rlen-1
while lidx<llen and ridx>=0:
    tmp=lSlist[lidx]+rSlist[ridx]
    if tmp==S:
        lcnt,rcnt=1,1
        lidx+=1
        ridx-=1
        while lidx<llen and lSlist[lidx]==lSlist[lidx-1]:
            lcnt+=1
            lidx+=1
        while ridx>=0 and rSlist[ridx]==rSlist[ridx+1]:
            rcnt+=1
            ridx-=1
        both+=lcnt*rcnt
    elif tmp<S:
        lidx+=1
    else:
        ridx-=1
print(lrans+both)

