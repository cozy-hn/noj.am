li=list(map(int,[*open(0)][:-1]))
for i in li:
    divisor=[]
    for j in range(1,i):
        if not i%j:
            divisor.append(j)
    if sum(divisor)==i:
        print(i,'= ',end='')
        print(*divisor,sep=' + ')
    else:
        print(i,'is NOT perfect.')