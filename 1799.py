N=int(input())
board=[list(map(int,input().split())) for _ in range(N)]
slash={i:True for i in range(2*N-1)}
backslash={i:True for i in range(-N+1,N)}
num,line,ans=0,0,0
def check(x,y):
    if slash[x+y] and backslash[x-y]:
        return True
    return False

def bishop(x,y,lim):
    global num, ans, line
    if num+lim-line<=ans:
        return
    if line==lim:
        ans=max(ans,num)
        return
    if y==N or (y==N-1 and x==-1):
        line+=1
        bishop(N-1,x+y-N+3,lim)
        line-=1
        return
    if x==-1:
        line+=1
        bishop(x+y+2,0,lim)
        line-=1
        return
    if board[y][x]==1:
        if check(x,y):
            slash[x+y]=False
            backslash[x-y]=False
            num+=1
            bishop(x-1,y+1,lim)
            slash[x+y]=True
            backslash[x-y]=True
            num-=1
    bishop(x-1,y+1,lim)
    return

bishop(0,0,N)
b=ans
num,line,ans=0,0,0
bishop(1,0,N-1)
w=ans
print(b+w)

# 0,0 1,0 2,0 3,0 4,0
# 0,1 1,1 2,1 3,1 4,1
# 0,2 1,2 2,2 3,2 4,2
# 0,3 1,3 2,3 3,3 4,3
# 0,4 1,4 2,4 3,4 4,4

# x+y
# 0 1 2 3 4
# 1 2 3 4 5
# 2 3 4 5 6
# 3 4 5 6 7
# 4 5 6 7 8

# x-y
# 0 1 2 3 4
# -1 0 1 2 3
# -2 -1 0 1 2
# -3 -2 -1 0 1
# -4 -3 -2 -1 0

# 3
# 0 1 1
# 1 1 1
# 1 1 1

# 4
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1

# 5
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1

# 8
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1

# 10
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1