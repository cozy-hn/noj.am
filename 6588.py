import sys

num=[True]*1000001
num[0]=False
num[1]=False
for i in range(2,int(1000001**0.5)+1):
    if num[i]:
        j=2
        while i*j<=1000000:
            num[i*j]=False
            j+=1
while True:
    N=int(sys.stdin.readline())
    if N==0:
        break
    for i in range(2,N//2+1):
        if num[i] and num[N-i]:
            print(N,'=',i,'+',N-i)
            break