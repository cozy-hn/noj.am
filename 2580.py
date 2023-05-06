plate=[[*map(int,input().split())] for _ in range(9)]

def ok(x,y):
    for i in range(9):
        if i!=y and plate[i][x]==plate[y][x]:
            return False
        if i!=x and plate[y][i]==plate[y][x]:
            return False
    tmpx=x//3
    tmpy=y//3
    for i in range(tmpy*3,tmpy*3+3):
        for j in range(tmpx*3,tmpx*3+3):
            if (i!=y and j!=x) and plate[i][j]==plate[y][x]:
                return False
    return True
idx=0
def backtrack():
    global idx
    global lenempty
    if idx>=lenempty:
        for i in range(9):
            print(*plate[i])
        exit()
    x,y=empty[idx]
    idx+=1
    for i in range(1,10):
        plate[y][x]=i
        if ok(x,y):
            backtrack()
        plate[y][x]=0
    idx-=1
empty=[(x,y) for y in range(9) for x in range(9) if plate[y][x]==0]


lenempty=len(empty)
backtrack()   
