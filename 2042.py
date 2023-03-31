import sys
input=lambda:sys.stdin.readline().rstrip()
N,M,K=map(int,input().split())
li=[0]*(N+1)
prefix_sum=[0]*(N+1)
for i in range(1,N+1):
    li[i]=int(input())
    prefix_sum[i]=prefix_sum[i-1]+li[i]
change=[]
for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1:
        change.append((b,c-li[b]))
        li[b]=c
    else:
        start,end=prefix_sum[b-1],prefix_sum[c]
        for i in change:
            if i[0]>b-1 and i[0]<=c:
                end+=i[1]
        print(end-start)