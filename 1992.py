import sys

input=lambda:sys.stdin.readline().rstrip()

def check(N,x,y):
    tmp=graph[y][x]
    for i in range(y,y+N):
        for j in range(x,x+N):
            if graph[i][j]!=tmp:
                return False
    return True


def dnq(N,x,y):
    if check(N,x,y):
        print(graph[y][x],end='')
    else:
        print('(',end='')
        dnq(N//2,x,y)
        dnq(N//2,x+N//2,y)
        dnq(N//2,x,y+N//2)
        dnq(N//2,x+N//2,y+N//2)
        print(')',end='')
    
N=int(input())
graph=[list(map(int,list(input()))) for _ in range(N)]
dnq(N,0,0)
