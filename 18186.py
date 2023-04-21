N,B,C=map(int,input().split())
ip=list(map(int,input().split()))
ans=0
if C>B:
    C=B
for i in range(N-2):
    while ip[i]!=0:
        if i==N-3 and ip[i+1]>0 and ip[i+2]>0:
            tmp=min(ip[i],ip[i+1],ip[i+2])
            ans+=tmp*(B+2*C)
            ip[i]-=tmp
            ip[i+1]-=tmp
            ip[i+2]-=tmp
        elif ip[i+1]>0 and ip[i+2]>0:
            if ip[i+3]==0:
                tmp=min(ip[i],ip[i+1],ip[i+2])
                ans+=tmp*(B+2*C)
                ip[i]-=tmp
                ip[i+1]-=tmp
                ip[i+2]-=tmp
            elif ip[i+1]>ip[i+2]:
                tmp=min(ip[i],ip[i+1]-ip[i+2])
                ans+=tmp*(B+C)
                ip[i]-=tmp
                ip[i+1]-=tmp
            else:
                tmp=min(ip[i],ip[i+1],ip[i+2])
                ans+=tmp*(B+2*C)
                ip[i]-=tmp
                ip[i+1]-=tmp
                ip[i+2]-=tmp
        elif ip[i+1]>0:
            tmp=min(ip[i],ip[i+1])
            ans+=tmp*(B+C)
            ip[i]-=tmp
            ip[i+1]-=tmp
        else:
            ans+=ip[i]*B
            ip[i]=0
while ip[N-2]!=0:
    if ip[N-1]>0:
        tmp=min(ip[N-2],ip[N-1])
        ans+=tmp*(B+C)
        ip[N-2]-=tmp
        ip[N-1]-=tmp
    else:
        ans+=ip[N-2]*B
        ip[N-2]=0
ans+=ip[N-1]*B
print(ans)
