import sys

input = lambda : sys.stdin.readline().rstrip()

def graph_check(N, x, y):
    flag=[False]*3
    for i in range(y,y+N):
        for j in range(x,x+N):
            if graph[i][j]==1:
                flag[0]=True
            elif graph[i][j]==-1:
                flag[1]=True
            elif graph[i][j]==0:
                flag[2]=True
        if flag.count(True)>=2:
            break
    if flag.count(True)==1:
        if flag[0]==True:
            return 1
        elif flag[1]==True:
            return 2
        elif flag[2]==True:
            return 3
    else:
        return 0
def bunhal(N, x, y):
    if N==1:
        if graph[y][x]==1:
            num[0]+=1
        elif graph[y][x]==-1:
            num[1]+=1
        elif graph[y][x]==0:
            num[2]+=1
        return
    full=graph_check(N,x,y)
    if full:
        if full==1:
            num[0]+=1
        elif full==2:
            num[1]+=1
        elif full==3:
            num[2]+=1
        return
    bunhal(N//3,x,y)
    bunhal(N//3,x+N//3,y)
    bunhal(N//3,x+N//3*2,y)
    bunhal(N//3,x,y+N//3)
    bunhal(N//3,x+N//3,y+N//3)
    bunhal(N//3,x+N//3*2,y+N//3)
    bunhal(N//3,x,y+N//3*2)
    bunhal(N//3,x+N//3,y+N//3*2)
    bunhal(N//3,x+N//3*2,y+N//3*2)
num=[0]*3
N=int(input())
graph=[list(map(int,input().split()))for _ in range(N)]
bunhal(N,0,0)
print(num[1],num[2],num[0],sep='\n')