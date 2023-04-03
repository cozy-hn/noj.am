import sys
input=lambda:sys.stdin.readline().rstrip()

def clockwise(Raph,tmp):
    for i in range(3):
        for j in range(3):
            tmp[j][2-i]=Raph[i][j]
    for i in range(3):
        for j in range(3):
            Raph[i][j]=tmp[i][j]


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

def ok(U,D,F,B,L,R):
    for i in range(3):
        for j in range(3):
            if U[i][j]!=U[0][0] or D[i][j]!=D[0][0] or F[i][j]!=F[0][0] or B[i][j]!=B[0][0] or L[i][j]!=L[0][0] or R[i][j]!=R[0][0]:
                return False
    return True

while True:
    s=input()
    if s=='ENDOFINPUT':
        exit()
    U=[input().split() for _ in range(3)]
    tmp=[input().split() for _ in range(3)]
    L=[tmp[i][:3] for i in range(3)]
    F=[tmp[i][3:6] for i in range(3)]
    R=[tmp[i][6:9] for i in range(3)]
    B=[tmp[i][9:] for i in range(3)]
    tmp=[['0']*3 for _ in range(3)]
    D=[input().split() for _ in range(3)]
    while True:
        t=input()
        if t=='END':
            if ok(U,D,F,B,L,R):
                print('Yes')
            else:
                print('No')
            break
        elif t=='front right':
            clockwise(F,tmp)
            swap_F(U,L,D,R)
        elif t=='front left':
            for _ in range(3):
                clockwise(F,tmp)
                swap_F(U,L,D,R)
        elif t=='left right':
            clockwise(L,tmp)
            swap_col(D,F,U,B,0)
        elif t=='left left':
            for _ in range(3):
                clockwise(L,tmp)
                swap_col(D,F,U,B,0)
        elif t=='right right':
            clockwise(R,tmp)
            swap_col(U,F,D,B,2)
        elif t=='right left':
            for _ in range(3):
                clockwise(R,tmp)
                swap_col(U,F,D,B,2)
        elif t=='back right':
            clockwise(B,tmp)
            swap_B(U,R,D,L)
        elif t=='back left':
            for _ in range(3):
                clockwise(B,tmp)
                swap_B(U,R,D,L)
        elif t=='top right':
            clockwise(U,tmp)
            swap_row(F,R,B,L,0)
        elif t=='top left':
            for _ in range(3):
                clockwise(U,tmp)
                swap_row(F,R,B,L,0)
        elif t=='bottom right':
            clockwise(D,tmp)
            swap_row(F,L,B,R,2)
        elif t=='bottom left':
            for _ in range(3):
                clockwise(D,tmp)
                swap_row(F,L,B,R,2)

