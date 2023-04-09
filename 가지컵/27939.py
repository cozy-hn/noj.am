import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
li=list(input().split())
dic={i+1:li[i] for i in range(n)}
ans=[]
m,k=map(int,input().split())
for _ in range(m):
    li2=list(map(int,input().split()))
    flag=False
    for i in li2:
        if dic[i]=='P':
            flag=True
            break
    if flag:
        ans.append('P')
    else:
        ans.append('W')
if 'W' in ans:
    print('W')
else:
    print('P')