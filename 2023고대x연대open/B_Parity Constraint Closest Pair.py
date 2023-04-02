import sys
input=lambda:sys.stdin.readline().rstrip()
N=int(input())
li=list(map(int,input().split()))
li.sort()
e=o=10**9*3
d=[li[i]-li[i-1] for i in range(1,N)]
for i in range(N-1):
    if d[i]%2==0 and d[i]<e:
        e=d[i]
    elif d[i]%2==1 and d[i]<o:
        o=d[i]
    if i>0 and d[i-1]%2==1 and d[i]%2==1 and e>d[i-1]+d[i]:
        e=d[i]+d[i-1]
if e==10**9*3:
    e=-1
if o==10**9*3:
    o=-1
print(e,o)