import sys
from collections import deque

input=lambda:sys.stdin.readline().rstrip()

def makefour(stri):
    stri=(4-len(stri))*'0'+stri
    return stri

for _ in range(int(input())):
    src,dst=input().split()
    src=makefour(src)
    dst=makefour(dst)
    dq=deque([src])
    visit=[(-1,'-1')]*10000
    visit[int(src)]=(0,'0')
    while dq:
        strx=dq.popleft()
        if strx==dst:
            break
        for i in ['D','S','L','R']:
            intstrx=int(strx)
            if i=='D':
                tmpstr=(intstrx*2)%10000
            elif i=='S':
                tmpstr=intstrx-1
                if tmpstr==-1:
                    tmpstr=9999
            elif i=='L':
                tmpstr=int(strx[1:]+strx[0])
            else:
                tmpstr=int(strx[3]+strx[:3])
            if visit[tmpstr][0]==-1:
                dq.append(makefour(str(tmpstr)))
                visit[tmpstr]=(intstrx,i)
    intdst=int(dst)
    ans=[]
    while True:
        if visit[intdst][1]=='0':
            break
        else:
            ans.append(visit[intdst][1])
            intdst=visit[intdst][0]
    print(*ans[::-1],sep='')