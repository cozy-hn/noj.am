import sys
from collections import deque
input= lambda : sys.stdin.readline().rstrip()
d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11=map(int,input().split())
graph=[[[[[[[[[[list(map(int,input().split())) for _ in range(d2)] for _ in range(d3)] for _ in range(d4)] for _ in range(d5)] for _ in range(d6)] for _ in range(d7)] for _ in range(d8)] for _ in range(d9)] for _ in range(d10)] for _ in range(d11)]
dq=deque()
tomato=0
empty=0
for x11 in range(d11):
    for x10 in range(d10):
        for x9 in range(d9):
            for x8 in range(d8):
                for x7 in range(d7):
                    for x6 in range(d6):
                        for x5 in range(d5):
                            for x4 in range(d4):
                                for x3 in range(d3):
                                    for x2 in range(d2):
                                        for x1 in range(d1):
                                            if graph[x11][x10][x9][x8][x7][x6][x5][x4][x3][x2][x1]==0:
                                                tomato+=1
                                            elif graph[x11][x10][x9][x8][x7][x6][x5][x4][x3][x2][x1]==-1:
                                                empty+=1
                                            else:
                                                dq.append((x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11))
dd1=[1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dd2=[0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dd3=[0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dd4=[0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dd5=[0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0,0,0]
dd6=[0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0,0,0]
dd7=[0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0,0,0]
dd8=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0,0,0]
dd9=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0,0,0]
dd10=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1,0,0]
dd11=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,-1]

if tomato+empty==d1*d2*d3*d4*d5*d6*d7*d8*d9*d10*d11:
    print(-1)
else:
    while dq:
        t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11=dq.popleft()
        for i in range(22):
            tmpt1=t1+dd1[i]  
            tmpt2=t2+dd2[i]
            tmpt3=t3+dd3[i]
            tmpt4=t4+dd4[i]  
            tmpt5=t5+dd5[i]
            tmpt6=t6+dd6[i]
            tmpt7=t7+dd7[i]  
            tmpt8=t8+dd8[i]
            tmpt9=t9+dd9[i]
            tmpt10=t10+dd10[i]  
            tmpt11=t11+dd11[i]
            if 0<=tmpt1<d1 and 0<=tmpt2<d2 and 0<=tmpt3<d3 and 0<=tmpt4<d4 and 0<=tmpt5<d5 and 0<=tmpt6<d6 and 0<=tmpt7<d7 and 0<=tmpt8<d8 and 0<=tmpt9<d9 and 0<=tmpt10<d10 and 0<=tmpt11<d11 and graph[tmpt11][tmpt10][tmpt9][tmpt8][tmpt7][tmpt6][tmpt5][tmpt4][tmpt3][tmpt2][tmpt1]==0:
                graph[tmpt11][tmpt10][tmpt9][tmpt8][tmpt7][tmpt6][tmpt5][tmpt4][tmpt3][tmpt2][tmpt1]=graph[t11][t10][t9][t8][t7][t6][t5][t4][t3][t2][t1]+1
                dq.append((tmpt1,tmpt2,tmpt3,tmpt4,tmpt5,tmpt6,tmpt7,tmpt8,tmpt9,tmpt10,tmpt11))
                tomato-=1
                
    if tomato:
        print(-1)
    else:
        print(graph[t11][t10][t9][t8][t7][t6][t5][t4][t3][t2][t1]-1)