graph=[list(input()) for _ in range(6)]
visit=[['N']*6 for _ in range(6)]
flag=True
for i in range(6):
    for j in range(6):
        if graph[i][j]!='.' and j<=2 and (i!=0 and i!=5) and (graph[i][j+1]!='.' and graph[i][j+2]!='.' and graph[i][j+3]!='.'):
            if graph[i-1][j:j+4].count('.')==3 and graph[i+1][j:j+4].count('.')==3:
                visit[i][j],visit[i][j+1],visit[i][j+2],visit[i][j+3]='D','R','U','L'
                for k in range(4):
                    if graph[i-1][j+k]!='.':
                        visit[i-1][j+k]='B'
                for k in range(4):
                    if graph[i+1][j+k]!='.':
                        visit[i+1][j+k]='F'
                flag=False
                break
        elif graph[i][j]!='.' and i<=2 and (j!=0 and j!=5) and (graph[i+1][j]!='.' and graph[i+2][j]!='.' and graph[i+3][j]!='.'):
            countl,countr=0,0
            tmpl,tmpr=0,0
            for k in range(4):
                if graph[i+k][j-1]!='.':
                    countl+=1
                    tmpl=i+k
                if graph[i+k][j+1]!='.':
                    countr+=1
                    tmpr=i+k
            if countl==1 and countr==1:
                visit[i][j],visit[i+1][j],visit[i+2][j],visit[i+3][j]='D','R','U','L'
                visit[tmpl][j-1],visit[tmpr][j+1]='F','B'
                flag=False
                break
        elif i!=0 and j<=1 and graph[i][j]!='.' and graph[i][j+1]!='.' and graph[i][j+2]!='.' and graph[i-1][j+2]!='.' and graph[i-1][j+3]!='.' and graph[i-1][j+4]!='.':
            visit[i][j],visit[i][j+1],visit[i][j+2],visit[i-1][j+2],visit[i-1][j+3],visit[i-1][j+4]='D','R','U','B','L','F'
            flag=False
            break
        elif i!=5 and j<=1 and graph[i][j]!='.' and graph[i][j+1]!='.' and graph[i][j+2]!='.' and graph[i+1][j+2]!='.' and graph[i+1][j+3]!='.' and graph[i+1][j+4]!='.':
            visit[i][j],visit[i][j+1],visit[i][j+2],visit[i+1][j+2],visit[i+1][j+3],visit[i+1][j+4]='D','R','U','F','L','B'
            flag=False
            break
        if j!=5 and i<=1:
            if graph[i][j]!='.' and graph[i+1][j]!='.' and graph[i+2][j]!='.' and graph[i+2][j+1]!='.' and graph[i+3][j+1]!='.' and graph[i+4][j+1]!='.':
                visit[i][j],visit[i+1][j],visit[i+2][j],visit[i+2][j+1],visit[i+3][j+1],visit[i+4][j+1]='D','R','U','B','L','F'
                flag=False
            elif graph[i][j]!='.' and graph[i+1][j]!='.' and graph[i+2][j]!='.' and graph[i+2][j-1]!='.' and graph[i+3][j-1]!='.' and graph[i+4][j-1]!='.':
                visit[i][j],visit[i+1][j],visit[i+2][j],visit[i+2][j-1],visit[i+3][j-1],visit[i+4][j-1]='D','R','U','F','L','B'
                flag=False
        if graph[i][j]!='.' and j<=3 and (i!=0 and i!=5) and (graph[i][j+1]!='.' and graph[i][j+2]!='.'):
            if graph[i-1][j:j+3].count('.')==2 and graph[i+1][j:j+3].count('.')==2 and not (graph[i-1][j+1]!='.' and graph[i+1][j+1]!='.'):
                if j!=0 and graph[i-1][j]!='.' and graph[i-1][j-1]!='.':
                    flag=False
                    visit[i][j],visit[i][j+1],visit[i][j+2],visit[i-1][j],visit[i-1][j-1]='D','R','U','B','L'
                    for k in range(3):
                        if graph[i+1][j+k]!='.':
                            visit[i+1][j+k]='F'
                elif j!=0 and graph[i+1][j]!='.' and graph[i+1][j-1]!='.':
                    flag=False
                    visit[i][j],visit[i][j+1],visit[i][j+2],visit[i+1][j],visit[i+1][j-1]='D','R','U','F','L'
                    for k in range(3):
                        if graph[i-1][j+k]!='.':
                            visit[i-1][j+k]='B'
                elif j!=3 and graph[i-1][j+2]!='.' and graph[i-1][j+3]!='.':
                    flag=False
                    visit[i][j],visit[i][j+1],visit[i][j+2],visit[i-1][j+2],visit[i-1][j+3]='D','R','U','B','L'
                    for k in range(3):
                        if graph[i+1][j+k]!='.':
                            visit[i+1][j+k]='F'
                elif j!=3 and graph[i+1][j+2]!='.' and graph[i+1][j+3]!='.':
                    flag=False
                    visit[i][j],visit[i][j+1],visit[i][j+2],visit[i+1][j+2],visit[i+1][j+3]='D','R','U','F','L'
                    for k in range(3):
                        if graph[i-1][j+k]!='.':
                            visit[i-1][j+k]='B'
        if graph[i][j]!='.' and i<=3 and (j!=0 and j!=5) and (graph[i+1][j]!='.' and graph[i+2][j]!='.'):
            countl,countr=0,0
            tmpl,tmpr=0,0
            for k in range(3):
                if graph[i+k][j-1]!='.':
                    countl+=1
                    tmpl=i+k
                if graph[i+k][j+1]!='.':
                    countr+=1
                    tmpr=i+k
            if countl==1 and countr==1 and not (tmpl==i+1 and tmpr==i+1):
                if i!=0 and graph[i][j-1]!='.' and graph[i-1][j-1]!='.':
                    flag=False
                    visit[i][j],visit[i+1][j],visit[i+2][j],visit[i][j-1],visit[i-1][j-1]='D','R','U','F','L'
                    for k in range(3):
                        if graph[i+k][j+1]!='.':
                            visit[i+k][j+1]='B'
                elif i!=0 and graph[i][j+1]!= '.' and graph[i-1][j+1]!='.':
                    flag=False
                    visit[i][j],visit[i+1][j],visit[i+2][j],visit[i][j+1],visit[i-1][j+1]='D','R','U','B','L'
                    for k in range(3):
                        if graph[i+k][j-1]!='.':
                            visit[i+k][j-1]='F'
                elif i!=3 and graph[i+2][j-1]!='.' and graph[i+3][j-1]!='.':
                    flag=False
                    visit[i][j],visit[i+1][j],visit[i+2][j],visit[i+2][j-1],visit[i+3][j-1]='D','R','U','F','L'
                    for k in range(3):
                        if graph[i+k][j+1]!='.':
                            visit[i+k][j+1]='B'
                elif i!=3 and graph[i+2][j+1]!='.' and graph[i+3][j+1]!='.':
                    flag=False
                    visit[i][j],visit[i+1][j],visit[i+2][j],visit[i+2][j+1],visit[i+3][j+1]='D','R','U','B','L'
                    for k in range(3):
                        if graph[i+k][j-1]!='.':
                            visit[i+k][j-1]='F'
        if j<=2 and i>=2 and graph[i][j]!='.' and graph[i][j+1]!='.' and graph[i-1][j+1]!='.' and graph[i-1][j+2]!='.' and graph[i-2][j+2]!='.' and graph[i-2][j+3]!='.':
            visit[i][j],visit[i][j+1],visit[i-1][j+1],visit[i-1][j+2],visit[i-2][j+2],visit[i-2][j+3]='D','R','B','U','L','F'
            flag=False
            break
        elif j<=2 and i<=3 and graph[i][j]!='.' and graph[i][j+1]!='.' and graph[i+1][j+1]!='.' and graph[i+1][j+2]!='.' and graph[i+2][j+2]!='.' and graph[i+2][j+3]!='.':
            visit[i][j],visit[i][j+1],visit[i+1][j+1],visit[i+1][j+2],visit[i+2][j+2],visit[i+2][j+3]='D','R','B','U','L','F'
            flag=False
            break
        elif i>=3 and j<=3 and graph[i][j]!='.' and graph[i-1][j]!='.' and graph[i-1][j+1]!='.' and graph[i-2][j+1]!='.' and graph[i-2][j+2]!='.' and graph[i-3][j+2]!='.':
            visit[i][j],visit[i-1][j],visit[i-1][j+1],visit[i-2][j+1],visit[i-2][j+2],visit[i-3][j+2]='D','R','B','U','L','F'
            flag=False
            break
        elif i<=2 and j<=3 and graph[i][j]!='.' and graph[i+1][j]!='.' and graph[i+1][j+1]!='.' and graph[i+2][j+1]!='.' and graph[i+2][j+2]!='.' and graph[i+3][j+2]!='.':
            visit[i][j],visit[i+1][j],visit[i+1][j+1],visit[i+2][j+1],visit[i+2][j+2],visit[i+3][j+2]='D','R','B','U','L','F'
            flag=False
            break
    if not flag:
        break
if flag:
    print('cannot fold')
else:              
	print('can fold')
            
# print(*visit,sep='\n') 