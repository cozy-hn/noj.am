import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    num=list(map(int,input().split()))
    ans=0
    MAX=num[-1]
    for i in range(N-2,-1,-1):
        if MAX<num[i]:
            MAX=num[i]
        else:
            ans+=MAX-num[i]
    print(ans)
