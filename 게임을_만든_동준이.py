import sys
input = lambda: sys.stdin.readline()
n=int(input())
lst=[int(input()) for _ in range(n)]
ans=0
for i in range(n-1,0,-1):
	if lst[i]<=lst[i-1]:
		ans+=lst[i-1]-lst[i]+1
		lst[i-1]=lst[i]-1
print(ans)