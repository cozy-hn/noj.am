N,M=map(int,input().split())
graph,visited=[[*map(int,input().split())] for _ in range(N)],[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            visited[i][j]=100
for i in range(N):
    for j in range(M):
        if visited[i][j]!=0 and i!=N-1:
            if graph[i+1][j]==0:
                visited[i+1][j]+=visited[i][j]
            elif graph[i+1][j]==1:
                if j!=0 and graph[i][j-1]==0 and graph[i+1][j-1]==0:
                    visited[i+1][j-1]+=visited[i][j]/2
                if j!=M-1 and graph[i][j+1]==0 and graph[i+1][j+1]==0:
                    visited[i+1][j+1]+=visited[i][j]/2
for i in visited[-1]:
    if i!=0:
        break
else:
    print(-1)
    exit()
print(visited[-1].index(max(visited[-1])))