N=int(input())
now=[*map(int,input())]
want=[*map(int,input())]

tmp1=now[:]
tmp2=now[:]

def switch(tmp,i):
    if i==0:
        tmp[i+1]=1-tmp[i+1]
        tmp[i]=1-tmp[i]
    elif i==N-1:
        tmp[i-1]=1-tmp[i-1]
        tmp[i]=1-tmp[i]
    else:
        tmp[i-1]=1-tmp[i-1]
        tmp[i]=1-tmp[i]
        tmp[i+1]=1-tmp[i+1]

cnt1,cnt2=1,0
switch(tmp1,0)

for i in range(1,N):
    if tmp1[i-1]!=want[i-1]:
        switch(tmp1,i)
        cnt1+=1
    if tmp2[i-1]!=want[i-1]:
        switch(tmp2,i)
        cnt2+=1

if tmp1[-1]==want[-1] and tmp2[-1]==want[-1]:
    print(min(cnt1,cnt2))
elif tmp1[-1]==want[-1]:
    print(cnt1)
elif tmp2[-1]==want[-1]:
    print(cnt2)
else:
    print(-1)