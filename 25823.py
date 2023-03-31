p=10**9+7
M=int(input())
f=[1]*(2*M+1)
for i in range(2,2*M+1):f[i]=f[i-1]*i%p
def combi(n):
    a=f[2*n];b=(f[n]*f[n])%p
    return (a*pow(b,p-2,p))%p
ans=0
for n in range(3,M+1):
    ans=(ans%p+(combi(n)%p))%p
print(ans%p)