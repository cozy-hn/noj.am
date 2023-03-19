li=[['']*15 for _ in range(5)]
for i in range(5):
    sli=list(input())
    for j in range(len(sli)):
        li[i][j]=sli[j]
for i in range(15):
    for j in range(5):
        print(li[j][i],end='')