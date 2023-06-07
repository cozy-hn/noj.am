import sys
input=sys.stdin.readline

N=int(input())
li=[int(input()) for _ in range(N)]
li.sort()
N=float(N*0.15)
def round(N):
    if N-int(N)>=0.5:
        return int(N)+1
    else:
        return int(N)
N=round(N)
if N==0:
    print(round(sum(li)/len(li)) if len(li) else 0)
else:
    li=li[N:-N]
    print(round(sum(li)/len(li)))
