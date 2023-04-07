def backtracking(x,start,add,minus,mul,div):
    if x==N-1:
        ans.append(start)
    else:
        if add>0:
            backtracking(x+1,start+num[x+1],add-1,minus,mul,div)
        if minus>0:
            backtracking(x+1,start-num[x+1],add,minus-1,mul,div)
        if mul>0:
            backtracking(x+1,start*num[x+1],add,minus,mul-1,div)
        if div>0:
            if start<0:
                backtracking(x+1,-((-start)//num[x+1]),add,minus,mul,div-1)
            else:
                backtracking(x+1,start//num[x+1],add,minus,mul,div-1)
N=int(input())
num=list(map(int,input().split()))
op=list(map(int,input().split()))
ans=[]

backtracking(0,num[0],op[0],op[1],op[2],op[3])
print(max(ans))
print(min(ans))