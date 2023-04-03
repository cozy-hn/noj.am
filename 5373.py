import sys
input=lambda:sys.stdin.readline().rstrip()

def clockwise(graph,tmp):
    for i in range(3):
        for j in range(3):
            tmp[j][2-i]=graph[i][j]
    for i in range(3):
        for j in range(3):
            graph[i][j]=tmp[i][j]


def swap_row(g1,g2,g3,g4,n):
    tmp=g1[n][:]
    g1[n]=g2[n][:]
    g2[n]=g3[n][:]
    g3[n]=g4[n][:]
    g4[n]=tmp[:]

def swap_col(g1,g2,g3,g4,n):
    tmp=[g1[i][n] for i in range(3)]
    for i in range(3):
        g1[i][n]=g2[i][n]
        g2[i][n]=g3[i][n]
        g3[i][n]=g4[2-i][2-n]
        g4[2-i][2-n]=tmp[i]


def swap_F(U,L,D,R):
    tmp=U[2][:]
    for i in range(3):
        U[2][i]=L[2-i][2]
        L[2-i][2]=D[0][2-i]
        D[0][2-i]=R[i][0]
        R[i][0]=tmp[i]

def swap_B(U,R,D,L):
    tmp=U[0][:]
    for i in range(3):
        U[0][i]=R[i][2]
        R[i][2]=D[2][2-i]
        D[2][2-i]=L[2-i][0]
        L[2-i][0]=tmp[i]

for _ in range(int(input())):
    GU=[['w']*3 for _ in range(3)]
    GD=[['y']*3 for _ in range(3)]
    GF=[['r']*3 for _ in range(3)]
    GB=[['o']*3 for _ in range(3)]
    GL=[['g']*3 for _ in range(3)]
    GR=[['b']*3 for _ in range(3)]
    tmp=[['0']*3 for _ in range(3)]
    N=int(input())
    order=list(input().split())
    for i in order:
        if i=='U+':
            clockwise(GU,tmp)
            swap_row(GF,GR,GB,GL,0)
        elif i=='U-':
            for _ in range(3):
                clockwise(GU,tmp)
                swap_row(GF,GR,GB,GL,0)
        elif i=='D+':
            clockwise(GD,tmp)
            swap_row(GF,GL,GB,GR,2)
        elif i=='D-':
            for _ in range(3):
                clockwise(GD,tmp)
                swap_row(GF,GL,GB,GR,2)
        elif i=='R+':
            clockwise(GR,tmp)
            swap_col(GU,GF,GD,GB,2)
        elif i=='R-':
            for _ in range(3):
                clockwise(GR,tmp)
                swap_col(GU,GF,GD,GB,2)
        elif i=='L+':
            clockwise(GL,tmp)
            swap_col(GD,GF,GU,GB,0)
        elif i=='L-':
            for _ in range(3):
                clockwise(GL,tmp)
                swap_col(GD,GF,GU,GB,0)
        elif i=='F+':
            clockwise(GF,tmp)
            swap_F(GU,GL,GD,GR)
        elif i=='F-':
            for _ in range(3):
                clockwise(GF,tmp)
                swap_F(GU,GL,GD,GR)
        elif i=='B+':
            clockwise(GB,tmp)
            swap_B(GU,GR,GD,GL)
        elif i=='B-':
            for _ in range(3):
                clockwise(GB,tmp)
                swap_B(GU,GR,GD,GL)
    for i in range(3):
        print(*GU[i],sep='')



