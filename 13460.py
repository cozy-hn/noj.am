from collections import deque
N,M=map(int,input().split())
Map=[list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Map[i][j]=='R':
            R=(j,i)
            Map[i][j]='.'
        elif Map[i][j]=='B':
            B=(j,i)
            Map[i][j]='.'
        elif Map[i][j]=='O':
            O=(j,i)
mv=['U','D','L','R']
visit=[(R[0],R[1],B[0],B[1])]
dq=deque([[R,B,0]])
while True:
    # print(dq)
    if not dq:
        print(-1)
        exit()
    dR,dB,cnt=dq.popleft()
    if cnt>=10:
        print(-1)
        exit()
    dRx,dRy,dBx,dBy=dR[0],dR[1],dB[0],dB[1]
    for i in mv:
        ddRx,ddRy,ddBx,ddBy=dRx,dRy,dBx,dBy
        flag=True
        if i=='U':
            if ddRx==ddBx:
                if ddBy>ddRy:
                    while True:
                        if Map[ddRy-1][ddRx]!='#':
                            ddRy-=1
                        else:
                            break
                        if Map[ddRy][ddRx]=='O':
                            while True:
                                if Map[ddBy-1][ddBx]!='#':
                                    ddBy-=1
                                else:
                                    break
                                if Map[ddBy][ddBx]=='O':
                                    flag=False
                                    break
                            if flag:
                                print(cnt+1)
                                exit()
                    while True:
                        if Map[ddBy-1][ddBx]!='#' and not (ddBx==ddRx and ddBy-1==ddRy):
                            ddBy-=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:
                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
                else:
                    while True:
                        if Map[ddBy-1][ddBx]!='#':
                            ddBy-=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:
                        while True:
                            if Map[ddRy-1][ddRx]!='#' and not (ddBx==ddRx and ddBy==ddRy-1):
                                ddRy-=1
                            else:
                                break
                            if Map[ddRy][ddRx]=='O':
                                print(cnt+1)
                                exit()
                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
            else:
                while True:
                    if Map[ddRy-1][ddRx]!='#':
                        ddRy-=1
                    else:
                        break
                    if Map[ddRy][ddRx]=='O':
                        print(cnt+1)
                        exit()
                while True:
                    if Map[ddBy-1][ddBx]!='#':
                        ddBy-=1
                    else:
                        break
                    if Map[ddBy][ddBx]=='O':
                        flag=False
                        break
                if flag:
                    if (ddRx,ddRy,ddBx,ddBy) not in visit:
                        visit.append((ddRx,ddRy,ddBx,ddBy))
                        dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
        elif i=='D':
            if ddRx==ddBx:
                if ddRy>ddBy:
                    while True:
                        if Map[ddRy+1][ddRx]!='#':
                            ddRy+=1
                        else:
                            break
                        if Map[ddRy][ddRx]=='O':
                            while True:
                                if Map[ddBy+1][ddBx]!='#':
                                    ddBy+=1
                                else:
                                    break
                                if Map[ddBy][ddBx]=='O':
                                    flag=False
                                    break
                            if flag:
                                print(cnt+1)
                                exit()
                    while True:
                        if Map[ddBy+1][ddBx]!='#' and not (ddBx==ddRx and ddBy+1==ddRy):
                            ddBy+=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:
                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
                else:
                    while True:
                        if Map[ddBy+1][ddBx]!='#':
                            ddBy+=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:
                        while True:
                            if Map[ddRy+1][ddRx]!='#' and not (ddBx==ddRx and ddBy==ddRy+1):
                                ddRy+=1
                            else:
                                break
                            if Map[ddRy][ddRx]=='O':
                                print(cnt+1)
                                exit()
                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
            else:
                while True:
                    if Map[ddRy+1][ddRx]!='#':
                        ddRy+=1
                    else:
                        break
                    if Map[ddRy][ddRx]=='O':
                        print(cnt+1)
                        exit()
                while True:
                    if Map[ddBy+1][ddBx]!='#':
                        ddBy+=1
                    else:
                        break
                    if Map[ddBy][ddBx]=='O':
                        flag=False
                        break
                if flag:
                    if (ddRx,ddRy,ddBx,ddBy) not in visit:
                        visit.append((ddRx,ddRy,ddBx,ddBy))
                        dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
        elif i=='L':
            if ddRy==ddBy:
                if ddRx<ddBx:
                    while True:
                        if Map[ddRy][ddRx-1]!='#':
                            ddRx-=1
                        else:
                            break
                        if Map[ddRy][ddRx]=='O':
                            while True:
                                if Map[ddBy][ddBx-1]!='#':
                                    ddBx-=1
                                else:
                                    break
                                if Map[ddBy][ddBx]=='O':
                                    flag=False
                                    break
                            if flag:
                                print(cnt+1)
                                exit()
                    while True:
                        if Map[ddBy][ddBx-1]!='#' and not (ddBx-1==ddRx and ddBy==ddRy):
                            ddBx-=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:

                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
                else:
                    while True:
                        if Map[ddBy][ddBx-1]!='#':
                            ddBx-=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:
                        while True:
                            if Map[ddRy][ddRx-1]!='#' and not (ddBx==ddRx-1 and ddBy==ddRy):
                                ddRx-=1
                            else:
                                break
                            if Map[ddRy][ddRx]=='O':
                                print(cnt+1)
                                exit()
                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
            else:
                while True:
                    if Map[ddRy][ddRx-1]!='#':
                        ddRx-=1
                    else:
                        break
                    if Map[ddRy][ddRx]=='O':
                        print(cnt+1)
                        exit()
                while True:
                    if Map[ddBy][ddBx-1]!='#':
                        ddBx-=1
                    else:
                        break
                    if Map[ddBy][ddBx]=='O':
                        flag=False
                        break
                if flag:
                    if (ddRx,ddRy,ddBx,ddBy) not in visit:
                        visit.append((ddRx,ddRy,ddBx,ddBy))
                        dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
        elif i=='R':
            if ddRy==ddBy:
                if ddRx>ddBx:
                    while True:
                        if Map[ddRy][ddRx+1]!='#':
                            ddRx+=1
                        else:
                            break
                        if Map[ddRy][ddRx]=='O':
                            while True:
                                if Map[ddBy][ddBx+1]!='#':
                                    ddBx+=1
                                else:
                                    break
                                if Map[ddBy][ddBx]=='O':
                                    flag=False
                                    break
                            if flag:
                                print(cnt+1)
                                exit()
                    while True:
                        if Map[ddBy][ddBx+1]!='#' and not (ddBx+1==ddRx and ddBy==ddRy):
                            ddBx+=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:
                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
                else:
                    while True:
                        if Map[ddBy][ddBx+1]!='#':
                            ddBx+=1
                        else:
                            break
                        if Map[ddBy][ddBx]=='O':
                            flag=False
                            break
                    if flag:
                        while True:
                            if Map[ddRy][ddRx+1]!='#' and not (ddBx==ddRx+1 and ddBy==ddRy):
                                ddRx+=1
                            else:
                                break
                            if Map[ddRy][ddRx]=='O':
                                print(cnt+1)
                                exit()
                        if (ddRx,ddRy,ddBx,ddBy) not in visit:
                            visit.append((ddRx,ddRy,ddBx,ddBy))
                            dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
            else:
                while True:
                    if Map[ddRy][ddRx+1]!='#':
                        ddRx+=1
                    else:
                        break
                    if Map[ddRy][ddRx]=='O':
                        print(cnt+1)
                        exit()
                while True:
                    if Map[ddBy][ddBx+1]!='#':
                        ddBx+=1
                    else:
                        break
                    if Map[ddBy][ddBx]=='O':
                        flag=False
                        break
                if flag:
                    if (ddRx,ddRy,ddBx,ddBy) not in visit:
                        visit.append((ddRx,ddRy,ddBx,ddBy))
                        dq.append([(ddRx,ddRy),(ddBx,ddBy),cnt+1])
