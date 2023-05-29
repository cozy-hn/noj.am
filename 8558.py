N=int(input())
ans=1
for i in range(1,N+1):
    ans=ans*i
    ans%=10
print(ans)