import sys
sys.setrecursionlimit(10**6)
input=lambda:sys.stdin.readline().rstrip()
a,b=map(int,input().split())
if a>b:
    a,b=b,a
fimtx=[[1,1],[1,0]]
mod=1000000000
def matrix_mul(N,a,b,mod):
    c=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c[i][j]=sum(a[i][k]*b[k][j] for k in range(N))%mod
    return c

def matrix_pow(A,Matrix,b,mod):
    if b==1:
        for i in range(A):
            for j in range(A):
                Matrix[i][j]%=mod
        return Matrix
    elif b%2==0:
        return matrix_pow(A,matrix_mul(A,Matrix,Matrix,mod),b//2,mod)
    else:
        return matrix_mul(A,Matrix,matrix_pow(A,matrix_mul(A,Matrix,Matrix,mod),b//2,mod),mod)

big=matrix_pow(2,fimtx,b+1,mod)
small=matrix_pow(2,fimtx,a,mod)
if big[0][0]==small[0][0]:
    print((big[0][0]-1)%mod)
else:
    print(((big[0][0]-1)%mod-(small[0][0]-1)%mod)%mod)