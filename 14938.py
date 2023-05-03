import sys
input=lambda:sys.stdin.readline()

def floywarshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

n,m,r=map(int,input().split())
item=list(map(int,input().split()))
dic={i+1:item[i] for i in range(n)}
INF=10**6
MAP=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(n+1):
	MAP[_][_]=0
for _ in range(r):
	a,b,c=map(int,input().split())
	MAP[a][b]=MAP[b][a]=c
floywarshall(MAP,n+1)
print(max(sum(dic[j] for j in range(1,n+1) if MAP[i][j]<=m) for i in range(1,n+1)))
