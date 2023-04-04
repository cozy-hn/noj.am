import sys
input=lambda:sys.stdin.readline().rstrip()

def e_gcd(a, b):
    x, y, u, v = 1, 0, 0, 1

    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, u = u, x - q * u
        y, v = v, y - q * v

    return a, x, y

for _ in range(int(input())):
    M,N,x,y=map(int,input().split())
    g,p,q=e_gcd(M,N)
    if (y-x)%g!=0:
        print(-1)
    else:
        mul=M*N
        ans=(x*N//g*q+y*M//g*p)%((M*N)//g)
        if ans:
           print(ans)
        else:
           print((M*N)//g)