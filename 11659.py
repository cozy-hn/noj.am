import sys
input=lambda:sys.stdin.readline().rstrip()
N,M=map(int,input().split())
li=list(map(int,input().split()))
prefix_sum=[0]*(N+1)
for i in range(len(li)):
    prefix_sum[i+1]=prefix_sum[i]+li[i]
for _ in range(M):
    a,b=map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])
    