N=int(input())
li=[0]*(N+1)
path={}
path[1]=1
path[2]=1
path[3]=1
if N==1:print(0)
elif N==2:print(1)
elif N==3:print(1)
else:
    li[2]=li[3]=1
    for i in range(4, len(li)):
        if i%2 and i%3:
            li[i]=li[i-1]+1
            path[i]=i-1
        elif not i%3 and not i%2:
            if li[i-1]<=li[i//3] and li[i-1]<=li[i//2]:
                li[i]=li[i-1]+1
                path[i]=i-1
            elif li[i//3]<=li[i-1] and li[i//3]<=li[i//2]:
                li[i]=li[i//3]+1
                path[i]=i//3
            elif li[i//2]<=li[i//3] and li[i//2]<=li[i-1]:
                li[i]=li[i//2]+1
                path[i]=i//2
        elif not i%3:
            if li[i-1]<=li[i//3]:
                li[i]=li[i-1]+1
                path[i]=i-1
            else:
                li[i]=li[i//3]+1
                path[i]=i//3
        elif not i%2:
            if li[i-1]<=li[i//2]:
                li[i]=li[i-1]+1
                path[i]=i-1
            else:
                li[i]=li[i//2]+1
                path[i]=i//2
    print(li[N])
while True:
    idx=N
    print(N,end=' ')
    if N==1:
        break
    N=path[N]