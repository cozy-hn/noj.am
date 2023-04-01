import sys
input=lambda:sys.stdin.readline().rstrip()
A,B=map(int,input().split())
Matrix=[list(map(int,input().split())) for _ in range(A)]

def matrix_mul(N,a,b):
    c=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c[i][j]=sum(a[i][k]*b[k][j] for k in range(N))%1000
    return c

def matrix_pow(A,Matrix,b):
    if b==1:
        for i in range(A):
            for j in range(A):
                Matrix[i][j]%=1000
        return Matrix
    elif b%2==0:
        return matrix_pow(A,matrix_mul(A,Matrix,Matrix),b//2)
    else:
        return matrix_mul(A,Matrix,matrix_pow(A,matrix_mul(A,Matrix,Matrix),b//2))

ans=matrix_pow(A,Matrix,B)
for i in ans:
    print(*i,sep=' ')
