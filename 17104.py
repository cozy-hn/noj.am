import sys
import math
input=sys.stdin.readline

num=[True]*1000001
num[0]=False
num[1]=False
for i in range(2,int(1000001**0.5)+1):
    if num[i]:
        j=2
        while i*j<=1000000:
            num[i*j]=False
            j+=1

def FFT(num):
    n=len(num)
    if n==1:
        return num
    w=math.exp((complex(0,(2*math.pi)/n)))
    Pe,Po=num[::2],num[1::2]
    ye,yo=FFT(Pe),FFT(Po)
    y=[0]*n
    for j in range(n//2):
        y[j]=ye[j]+w**j*yo[j]
        y[j+n//2]=ye[j]-w**j*yo[j]
    return y
print(FFT(num))
	
# T=int(input())
# for _ in range(T):
#     cnt=0
#     N=int(input())
#     for i in range(2,N//2+1):
#         if num[i] and num[N-i]:
#             cnt+=1
#     print(cnt)