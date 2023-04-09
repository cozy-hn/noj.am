L,C=map(int,input().split())
li=sorted(list(input().split()))
Str=''.join(li)

def backtracking(comb,Str):
    if len(comb)==L:
        if sum(1 for i in comb if i in 'aeiou')>=1 and sum(1 for i in comb if i not in 'aeiou')>=2:
            print(*comb,sep='')
        return
    for i in range(len(Str)):
        backtracking(comb+Str[i],Str[i+1:])

backtracking('',Str)