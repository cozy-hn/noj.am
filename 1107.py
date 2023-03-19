import sys

N=int(input())
M=int(input())
if M>1:
    flagk=True
    li=list(input().split())
    if M==9:
        for i in range(9):
            if str(i+1)!=li[i]:
                flagk=False
                break
        if flagk:
            print(min(N+1,abs(N-100)))
            sys.exit(0)
        
elif M==1:
    li=list(input())
else:
    li=[]
if M==10:
    print(abs(N-100))
    sys.exit(0)
idx=0
while True:
    flagp=True
    flagn=True
    for i in li:
        if i in str(N+idx):
            flagp=False
            break
    if N-idx>=0:
        for i in li:
            if i in str(N-idx):
                flagn=False
                break
    if N-idx<0:
        flagn=False
    if flagn:
        cnt = idx + len(str(N-idx))
        break
    elif flagp:
        cnt= idx + len(str(N+idx))
        break
    else:
        idx += 1
        if idx >= abs(N-100):
            cnt=500000
            break;
print(min(cnt,abs(N-100)))
