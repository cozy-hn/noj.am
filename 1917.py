for _ in range(3):
    graph=[list(map(int,input().split())) for _ in range(6)]
    flag=True
    for i in range(6):
        for j in range(6):
            if graph[i][j]!=0 and j<=2 and (i!=0 and i!=5) and (graph[i][j+1]!=0 and graph[i][j+2]!=0 and graph[i][j+3]!=0):
                if graph[i-1][j:j+4].count(0)==3 and graph[i+1][j:j+4].count(0)==3:
                    flag=False
                    break
            elif graph[i][j]!=0 and i<=2 and (j!=0 and j!=5) and (graph[i+1][j]!=0 and graph[i+2][j]!=0 and graph[i+3][j]!=0):
                countl,countr=0,0
                for k in range(4):
                    if graph[i+k][j-1]!=0:
                        countl+=1
                    if graph[i+k][j+1]!=0:
                        countr+=1
                if countl==1 and countr==1:
                    flag=False
                    break
            elif i!=0 and j<=1 and graph[i][j]!=0 and graph[i][j+1]!=0 and graph[i][j+2]!=0 and graph[i-1][j+2]!=0 and graph[i-1][j+3]!=0 and graph[i-1][j+4]!=0:
                flag=False
                break
            elif i!=5 and j<=1 and graph[i][j]!=0 and graph[i][j+1]!=0 and graph[i][j+2]!=0 and graph[i+1][j+2]!=0 and graph[i+1][j+3]!=0 and graph[i+1][j+4]!=0:
                flag=False
                break
            elif j!=5 and i<=1 and graph[i][j]!=0 and graph[i+1][j]!=0 and graph[i+2][j]!=0 and graph[i+2][j+1]!=0 and graph[i+3][j+1]!=0 and graph[i+4][j+1]!=0:
                flag=False
                break
            elif j!=0 and i<=1 and graph[i][j]!=0 and graph[i+1][j]!=0 and graph[i+2][j]!=0 and graph[i+2][j-1]!=0 and graph[i+3][j-1]!=0 and graph[i+4][j-1]!=0:
                flag=False
                break
            if graph[i][j]!=0 and j<=3 and (i!=0 and i!=5) and (graph[i][j+1]!=0 and graph[i][j+2]!=0):
                if graph[i-1][j:j+3].count(0)==2 and graph[i+1][j:j+3].count(0)==2 and not (graph[i-1][j+1]!=0 and graph[i+1][j+1]!=0):
                    if j!=0 and graph[i-1][j]!=0 and graph[i-1][j-1]!=0:
                        flag=False
                        break
                    elif j!=0 and graph[i+1][j]!=0 and graph[i+1][j-1]!=0:
                        flag=False
                        break
                    elif j!=3 and graph[i-1][j+2]!=0 and graph[i-1][j+3]!=0:
                        flag=False
                        break
                    elif j!=3 and graph[i+1][j+2]!=0 and graph[i+1][j+3]!=0:
                        flag=False
                        break
            if graph[i][j]!=0 and i<=3 and (j!=0 and j!=5) and (graph[i+1][j]!=0 and graph[i+2][j]!=0):
                countl,countr=0,0
                tmpl,tmpr=0,0
                for k in range(3):
                    if graph[i+k][j-1]!=0:
                        countl+=1
                        tmpl=i+k
                    if graph[i+k][j+1]!=0:
                        countr+=1
                        tmpr=i+k
                if countl==1 and countr==1 and not (tmpl==i+1 and tmpr==i+1):
                    if i!=0 and graph[i][j-1]!=0 and graph[i-1][j-1]!=0:
                        flag=False
                        break
                    elif i!=0 and graph[i][j+1]!= 0 and graph[i-1][j+1]!=0:
                        flag=False
                        break
                    elif i!=3 and graph[i+2][j-1]!=0 and graph[i+3][j-1]!=0:
                        flag=False
                        break
                    elif i!=3 and graph[i+2][j+1]!=0 and graph[i+3][j+1]!=0:
                        flag=False
                        break
            if j<=2 and i>=2 and graph[i][j]!=0 and graph[i][j+1]!=0 and graph[i-1][j+1]!=0 and graph[i-1][j+2]!=0 and graph[i-2][j+2]!=0 and graph[i-2][j+3]!=0:
                flag=False
                break
            elif j<=2 and i<=3 and graph[i][j]!=0 and graph[i][j+1]!=0 and graph[i+1][j+1]!=0 and graph[i+1][j+2]!=0 and graph[i+2][j+2]!=0 and graph[i+2][j+3]!=0:
                flag=False
                break
            elif i>=3 and j<=3 and graph[i][j]!=0 and graph[i-1][j]!=0 and graph[i-1][j+1]!=0 and graph[i-2][j+1]!=0 and graph[i-2][j+2]!=0 and graph[i-3][j+2]!=0:
                flag=False
                break
            elif i<=2 and j<=3 and graph[i][j]!=0 and graph[i+1][j]!=0 and graph[i+1][j+1]!=0 and graph[i+2][j+1]!=0 and graph[i+2][j+2]!=0 and graph[i+3][j+2]!=0:
                flag=False
                break
        if not flag:
            break
    if flag:
        print('no')
    else:              
        print('yes')
