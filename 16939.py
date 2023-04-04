import sys
input=lambda:sys.stdin.readline().rstrip()

def clockwise(Raph,tmp):
    for i in range(2):
        for j in range(2):
            tmp[j][1-i]=Raph[i][j]
    for i in range(2):
        for j in range(2):
            Raph[i][j]=tmp[i][j]


def swap_row(g1,g2,g3,g4,n):
    tmp=g1[n][:]
    g1[n]=g2[n][:]
    g2[n]=g3[n][:]
    g3[n]=g4[n][:]
    g4[n]=tmp[:]

def swap_col(g1,g2,g3,g4,n):
    tmp=[g1[i][n] for i in range(2)]
    for i in range(2):
        g1[i][n]=g2[i][n]
        g2[i][n]=g3[i][n]
        g3[i][n]=g4[1-i][1-n]
        g4[1-i][1-n]=tmp[i]


def swap_F(U,L,D,R):
    tmp=U[1][:]
    for i in range(2):
        U[1][i]=L[1-i][1]
        L[1-i][1]=D[0][1-i]
        D[0][1-i]=R[i][0]
        R[i][0]=tmp[i]

def swap_B(U,R,D,L):
    tmp=U[0][:]
    for i in range(2):
        U[0][i]=R[i][1]
        R[i][1]=D[1][1-i]
        D[1][1-i]=L[1-i][0]
        L[1-i][0]=tmp[i]

def ok(U,D,F,B,L,R):
    for i in range(2):
        for j in range(2):
            if U[i][j]!=U[0][0] or D[i][j]!=D[0][0] or F[i][j]!=F[0][0] or B[i][j]!=B[0][0] or L[i][j]!=L[0][0] or R[i][j]!=R[0][0]:
                return False
    return True
U=[[0]*2 for _ in range(2)]
F=[[0]*2 for _ in range(2)]
D=[[0]*2 for _ in range(2)]
L=[[0]*2 for _ in range(2)]
R=[[0]*2 for _ in range(2)]
B=[[0]*2 for _ in range(2)]
tmp=[[0]*2 for _ in range(2)]
ip=list(map(int,input().split()))
cnt=0
for j in range(2):
  for i in range(2):
    U[j][i]=ip[cnt]
    F[j][i]=ip[cnt+4]
    D[j][i]=ip[cnt+8]
    L[j][i]=ip[cnt+12]
    R[j][i]=ip[cnt+16]
    B[j][i]=ip[cnt+20]
    cnt+=1
clockwise(F,tmp)
swap_F(U,L,D,R)
if ok(U, D, F, B, L, R):
  print(1)
else:
    for _ in range(2):
        clockwise(F,tmp)
        swap_F(U,L,D,R)
    if ok(U, D, F, B, L, R):
        print(1)
    else:
        clockwise(F,tmp)
        swap_F(U,L,D,R)
        clockwise(L,tmp)
        swap_col(D,F,U,B,0)
        if ok(U, D, F, B, L, R):
            print(1)
        else:
            for _ in range(2):
                clockwise(L,tmp)
                swap_col(D,F,U,B,0)
            if ok(U, D, F, B, L, R):
                print(1)
            else:
              clockwise(L,tmp)
              swap_col(D,F,U,B,0)
              clockwise(R,tmp)
              swap_col(U,F,D,B,1)
              if ok(U, D, F, B, L, R):
                print(1)
              else:
                for _ in range(2):
                    clockwise(R,tmp)
                    swap_col(U,F,D,B,1)
                if ok(U, D, F, B, L, R):
                    print(1)
                else:
                    clockwise(R,tmp)
                    swap_col(U,F,D,B,1)
                    clockwise(B,tmp)
                    swap_B(U,R,D,L)
                    if ok(U, D, F, B, L, R):
                        print(1)
                    else:
                        for _ in range(2):
                            clockwise(B,tmp)
                            swap_B(U,R,D,L)
                        if ok(U, D, F, B, L, R):
                            print(1)
                        else:
                            clockwise(B,tmp)
                            swap_B(U,R,D,L)
                            clockwise(U,tmp)
                            swap_row(F,R,B,L,0)
                            if ok(U, D, F, B, L, R):
                                print(1)
                            else:
                                for _ in range(2):
                                    clockwise(U,tmp)
                                    swap_row(F,R,B,L,0)
                                if ok(U, D, F, B, L, R):
                                    print(1)
                                else:
                                    clockwise(U,tmp)
                                    swap_row(F,R,B,L,0)
                                    clockwise(D,tmp)
                                    swap_row(F,L,B,R,1)
                                    if ok(U, D, F, B, L, R):
                                        print(1)
                                    else:
                                        for _ in range(2):
                                            clockwise(D,tmp)
                                            swap_row(F,L,B,R,1)
                                        if ok(U, D, F, B, L, R):
                                            print(1)
                                        else:
                                            clockwise(D,tmp)
                                            swap_row(F,L,B,R,1)
                                            print(0)
