import sys
input=lambda:sys.stdin.readline().rstrip()
n,k=map(int,input().split())
people=list(map(int,input().split()))
if n==1:
    print(0)
    exit()
exhausted=[0]*n
for i in range(1,n-1):
    exhausted[i]=max(abs(people[i]-people[i-1]),abs(people[i]-people[i+1]))
exhausted[0]=abs(people[0]-people[1])
exhausted[-1]=abs(people[-1]-people[-2])
exhausted.sort(reverse=True)
tmp=list(set(exhausted[k:]))
tmp.sort()
if tmp:
    print(tmp[-1])
else:
	print(0)