import sys
input=lambda:sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
input=lambda:sys.stdin.readline().rstrip()
fimtx=[[1,1],[1,0]]
p=10**9
def matrix_mul(N,a,b,p):
    c=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            c[i][j]=sum(a[i][k]*b[k][j] for k in range(N))%p
    return c

def matrix_pow(A,Matrix,b,p):
    if b==1:
        for i in range(A):
            for j in range(A):
                Matrix[i][j]%=p
        return Matrix
    elif b%2==0:
        return matrix_pow(A,matrix_mul(A,Matrix,Matrix,p),b//2,p)
    else:
        return matrix_mul(A,Matrix,matrix_pow(A,matrix_mul(A,Matrix,Matrix,p),b//2,p),p)
for _ in range(int(input())):
    a,b=map(int,input().split())
    if b==1:
        ans=[[1,1],[1,0]]
    else:
        ans=matrix_pow(2,fimtx,b-1,p)
    print(a,ans[0][0])