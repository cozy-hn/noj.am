from copy import deepcopy

bulb=[bytearray(1<<1) for _ in range(10)]
dx=[0,0,0,1,-1]
dy=[0,1,-1,0,0]
    
def setbyte(y):
    line=input()
    for x in range(10):
        if line[x]=='O':
            bulb[y][x>>3]|=1<<(x&7)
            
def switch(y,x,tmp):
    for i in range(5):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<10 and 0<=nx<10:
            tmp[ny][nx>>3]^=1<<(nx&7)

for y in range(10):
    setbyte(y)

ans=101
for i in range(1<<10):
    tmp=deepcopy(bulb)
    cnt=0
    for j in range(10):
        if i&(1<<j):
            switch(0,j,tmp)
            cnt+=1
    for y in range(1,10):
        for x in range(10):
            if tmp[y-1][x>>3]&(1<<(x&7)):
                switch(y,x,tmp)
                cnt+=1
    for x in range(10):
        if tmp[9][x>>3]&(1<<(x&7)):
            cnt=101
            break
    ans=min(ans,cnt)
        

if ans==101:
    print(-1)
else:
    print(ans)