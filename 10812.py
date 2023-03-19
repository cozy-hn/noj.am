import sys
input=sys.stdin.readline
N,M=map(int,input().split())
li=[i for i in range(0,N+1)]
for _ in range(M):
    i,j,k=map(int,input().split())
    li=li[:i]+li[k:j+1]+li[i:k]+li[j+1:]
print(*li[1:])