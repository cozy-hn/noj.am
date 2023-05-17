R,C,T=map(int,input().split())
room=[list(map(int,input().split())) for _ in range(R)]
for y in range(R):
    if room[y][0]==-1:
        cleaner_up=y
        cleaner_down=y+1
        break
dy,dx=[-1,1,0,0],[0,0,-1,1]
def diffusion(R,C):
    tmp=[[0]*C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if room[y][x]>0:
                cnt=0
                for d in range(4):
                    ny,nx=y+dy[d],x+dx[d]
                    if 0<=ny<R and 0<=nx<C and room[ny][nx]!=-1:
                        tmp[ny][nx]+=room[y][x]//5
                        cnt+=1
                room[y][x]-=(room[y][x]//5)*cnt
    for y in range(R):
        for x in range(C):
            room[y][x]+=tmp[y][x]

def air_cleaner(up,down,R,C):
    for y in range(up-1,0,-1):
        room[y][0]=room[y-1][0]
    for x in range(C-1):
        room[0][x]=room[0][x+1]
    for y in range(up):
        room[y][C-1]=room[y+1][C-1]
    for x in range(C-1,1,-1):
        room[up][x]=room[up][x-1]
    room[up][1]=0
    for y in range(down+1,R-1):
        room[y][0]=room[y+1][0]
    for x in range(C-1):
        room[R-1][x]=room[R-1][x+1]
    for y in range(R-1,down,-1):
        room[y][C-1]=room[y-1][C-1]
    for x in range(C-1,1,-1):
        room[down][x]=room[down][x-1]
    room[down][1]=0

def dust_sum():
    return sum(sum(room[i]) for i in range(R))+2
    
for _ in range(T):
    diffusion(R,C)
    air_cleaner(cleaner_up,cleaner_down,R,C)    
print(dust_sum())