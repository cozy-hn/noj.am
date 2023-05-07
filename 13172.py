import sys
input = sys.stdin.readline

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

mod=1000000007
T=int(input())
ans=0
for _ in range(T):
    n,s=map(int,input().split())
    g=gcd(n,s)
    a,b = n//g, s//g
    inv_mod_a=pow(a,mod-2,mod)
    ans=(ans%mod+(b*inv_mod_a)%mod)%mod
print(ans)