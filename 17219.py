import sys
input=lambda:sys.stdin.readline().rstrip()
N,M=map(int,input().split())
dic={}
for _ in range(N):
    a,b=input().split()
    dic[a]=b
for _ in range(M):
    print(dic[input()])