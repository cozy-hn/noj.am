import sys
input=lambda:sys.stdin.readline().rstrip()

def check(N,x,y):
    flag0=flag1=False
    for i in range(y,y+N):
        for j in range(x,x+N):
            if li[i][j]==1:
                flag1=True
            else:
                flag0=True
            if flag1 and flag0:
                break
    if flag1 and flag0:
        return 0
    else:
        if flag1:
            return 1
        if flag0:
            return 2

def dnq(N,x,y):
    global blue
    global white
    if N==1:
        if li[y][x]==0:
            white+=1
        else:
            blue+=1
        return
    tmp=check(N,x,y)
    if tmp:
        if tmp==1:
            blue+=1
        elif tmp==2:
            white+=1
    else:
        dnq(N//2,x,y)
        dnq(N//2,x+N//2,y)
        dnq(N//2,x,y+N//2)
        dnq(N//2,x+N//2,y+N//2)
    
blue=0
white=0
N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
dnq(N,0,0)
print(white,blue,sep='\n')
