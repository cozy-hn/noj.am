import sys
sys.setrecursionlimit(10**6)
input=lambda:sys.stdin.readline().rstrip()

fimtx=[[1,1],[1,0]]
mod=10**9

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

for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(1)
    else:
        ans=matrix_pow(2,fimtx,n-1,mod)
        print(ans[0][0])