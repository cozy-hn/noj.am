from collections import deque

N=int(input())
Map=[list(input()) for _ in range(N)]
visited=set()
for i in range(0,N):
    for j in range(0,N):
        if Map[i][j]=='B':
            if 0<i<N-1 and (Map[i-1][j]=='B' and Map[i+1][j]=='B'):
                center=(i,j,0)
                visited.add(center)
            elif 0<j<N-1 and (Map[i][j-1]=='B' and Map[i][j+1]=='B'):
                center=(i,j,1)
                visited.add(center)
        if Map[i][j]=='E':
            if 0<i<N-1 and (Map[i-1][j]=='E' and Map[i+1][j]=='E'):
                end=(i,j,0)
            elif 0<j<N-1 and (Map[i][j-1]=='E' and Map[i][j+1]=='E'):
                end=(i,j,1)
dq=deque()
dq.append((center,0))
while dq:
    now, cnt=dq.popleft()
    for i in range(5):
        pos=-1
        if i==0: #U
            if now[2]==0:
                if now[0]>1 and Map[now[0]-2][now[1]]!='1' and (now[0]-1,now[1],0) not in visited:
                    tmpx, tmpy, pos = now[0]-1, now[1], 0
            else:
                if (now[0]>0 and 0<now[1]<N-1)and (Map[now[0]-1][now[1]]!='1' and Map[now[0]-1][now[1]-1]!='1' and Map[now[0]-1][now[1]+1]!='1')and (now[0]-1,now[1],1) not in visited:
                    tmpx, tmpy, pos = now[0]-1, now[1], 1
        elif i==1: #D
            if now[2]==0:
                if now[0]<N-2 and Map[now[0]+2][now[1]]!='1' and (now[0]+1,now[1],0) not in visited:
                    tmpx, tmpy, pos = now[0]+1, now[1], 0
            else:
                if (now[0]<N-1 and 0<now[1]<N-1) and (Map[now[0]+1][now[1]]!='1' and Map[now[0]+1][now[1]-1]!='1' and Map[now[0]+1][now[1]+1]!='1')and (now[0]+1,now[1],1) not in visited:
                    tmpx, tmpy, pos = now[0]+1, now[1], 1
        elif i==2: #L
            if now[2]==0:
                if (0<now[0]<N-1 and now[1]>0) and (Map[now[0]][now[1]-1]!='1' and Map[now[0]-1][now[1]-1]!='1' and Map[now[0]+1][now[1]-1]!='1')and (now[0],now[1]-1,1) not in visited:
                    tmpx, tmpy, pos = now[0], now[1]-1, 1
            else:
                if now[1]>1 and Map[now[0]][now[1]-2]!='1' and (now[0],now[1]-1,0) not in visited:
                    tmpx, tmpy, pos = now[0], now[1]-1, 0
        elif i==3: #R
            if now[2]==0:
                if (0<now[1]<N-1 and now[1]<N-1) and (Map[now[0]][now[1]+1]!='1' and Map[now[0]-1][now[1]+1]!='1' and Map[now[0]+1][now[1]+1]!='1')and (now[0],now[1]+1,1) not in visited:
                    tmpx, tmpy, pos = now[0], now[1]+1, 1
            else:
                if now[1]<N-2 and Map[now[0]][now[1]+2]!='1' and (now[0],now[1]+1,0) not in visited:
                    tmpx, tmpy, pos = now[0], now[1]+1, 0
        else: #T
            if 0<now[0]<N-1 and 0<now[1]<N-1 and Map[now[0]-1][now[1]]!='1' and Map[now[0]+1][now[1]]!='1' \
            and Map[now[0]][now[1]-1]!='1' and Map[now[0]][now[1]+1]!='1' and Map[now[0]-1][now[1]-1]!='1' and Map[now[0]-1][now[1]+1]!='1' \
            and Map[now[0]+1][now[1]-1]!='1' and Map[now[0]+1][now[1]+1]!='1'\
            and (now[0],now[1],(now[2]+1)%2) not in visited:
                tmpx, tmpy, pos = now[0], now[1], (now[2]+1)%2
        if pos!=-1:
            visited.add((tmpx,tmpy,pos))
            dq.append(((tmpx,tmpy,pos),cnt+1))
            if (tmpx,tmpy,pos)==end:
                print(cnt+1)
                exit()
print(0)