N=int(input())
road=list(map(int,input().split()))
price=list(map(int,input().split()))
ans=0
Min=price[0]
for i in range(N-1):
    Min=min(Min,price[i])
    ans+=Min*road[i]
print(ans)