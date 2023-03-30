N=int(input())
M=int(input())
S=input()
hey='I'+N*'OI'
rtn=0
start=-1
flag=False
while True:
    idx=S.find(hey,start+1)
    if idx==-1 or flag:
        break
    rtn+=1
    for i in range(idx+2*N,M,2):
        if i==M-1 or i+1==M-1:
            flag=True
            break
        if i+2==M-1:
            if S[i+1]=='O' and S[i+2]=='I':
                rtn+=1
            flag=True
            break
        if S[i+1]=='O' and S[i+2]=='I':
            rtn+=1
        else:
            start=i
            break
print(rtn)        