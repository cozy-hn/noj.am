import sys
input=lambda:sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
fimtx=[[1,1],[1,0]]
p=10**9+7
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

def GCD(x,y):
    while y:
        x,y=y,x%y
    return x

a,b=map(int,input().split())
n=GCD(a,b)
if n==1:
    print(1)
    exit()
ans=matrix_pow(2,fimtx,n-1,p)
print(ans[0][0])