num=[True]*1000001
num[0]=False
num[1]=False
for i in range(2,1000001):
    if num[i]:
        j=2
        while i*j<=1000000:
            num[i*j]=False
            j+=1
T=int(input())
for _ in range(T):
    cnt=0
    N=int(input())
    for i in range(2,N//2+1):
        if num[i] and num[N-i]:
            cnt+=1
    print(cnt)