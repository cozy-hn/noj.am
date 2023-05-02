import sys

input=sys.stdin.readline

def floywarshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

N,M=map(int,input().split())
INF=10**6
graph=[[INF]*N for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

floywarshall(graph,N)
ret=0
for i in range(N):
    for j in range(N):
        if graph[i][j]==INF and graph[j][i]==INF and i!=j:
            break
    else:
        ret+=1
print(ret)