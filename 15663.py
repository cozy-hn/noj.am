# import sys
# input=lambda:sys.stdin.readline().rstrip()

N,M=map(int,input().split())
li=[0]+list(map(int,input().split()))
li.sort()
ans = []
idx=[0]*M
ansset=set()
def dfs(p):
    if len(ans)==M:
        for i in range(M):
            idx[i]=li[ans[i]]
        ansset.add(tuple(idx))
        return
    for i in range(p,N+1):
        if i not in ans:
            ans.append(i)
            dfs(1)
            ans.pop()
dfs(1)
ansli=list(ansset)
ansli.sort()
for i in ansli:
    print(*i,sep=' ')