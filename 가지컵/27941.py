
import sys
input=lambda:sys.stdin.readline().rstrip()
Map=[list(map(int,input().split())) for _ in range(2047)]
Mm=[(max(Map[j][i] for j in range(2047)),(min(Map[j][i] for j in range(2047)))) for i in range(11)]
for i in range(2**11):
    li=[]
    for j in range(11):
        if i & (1 << j):
            li.append(Mm[j][1])
        else:
            li.append(Mm[j][0])
    if li not in Map:
        print(*li)
        break