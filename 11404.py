import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
INF=10**9
road=[[INF]*n for _ in range(n)]
for i in range(n):
    road[i][i]=0
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    road[a-1][b-1]=min(road[a-1][b-1],c)
for k in range(n):
    for y in range(n):
        for x in range(n):
            road[y][x]=min(road[y][k]+road[k][x],road[y][x])
for y in range(n):
    for x in range(n):
        if road[y][x]==INF:
            road[y][x]=0
for i in road:
    print(*i)