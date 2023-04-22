N=int(input())
ip=list(map(int,input().split()))
ans=[0]*N
stack=[0]
for i in range(1,N):
    if ip[stack[-1]]>ip[i]:
        ans[i]=stack[-1]+1
        stack.append(i)
    else:
        while stack and ip[stack[-1]]<=ip[i]:
            stack.pop()
        if not stack:
            ans[i]=0
        else:
            ans[i]=stack[-1]+1
        stack.append(i)
print(*ans)