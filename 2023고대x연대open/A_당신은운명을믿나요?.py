ip=input()
ip2=ip[:]
lenip=len(ip)
lenip2=len(ip2)
flagK=flagY=True
while True:
    idxY=ip.find('Y')
    if idxY==-1 or idxY==lenip-1:
        flagY=False
        break
    idxY=ip.find('O',idxY+1)
    if idxY==-1 or idxY==lenip-1:
        flagY=False
        break
    idxY=ip.find('N',idxY+1)
    if idxY==-1 or idxY==lenip-1:
        flagY=False
        break
    idxY=ip.find('S',idxY+1)
    if idxY==-1 or idxY==lenip-1:
        flagY=False
        break
    idxY=ip.find('E',idxY+1)
    if idxY==-1 or idxY==lenip-1:
        flagY=False
        break
    idxY=ip.find('I',idxY+1)
    break
while True:
    idxK=ip.find('K')
    if idxK==-1 or idxK==lenip2-1:
        flagK=False
        break
    idxK=ip.find('O',idxK+1)
    if idxK==-1 or idxK==lenip2-1:
        flagK=False
        break
    idxK=ip.find('R',idxK+1)
    if idxK==-1 or idxK==lenip2-1:
        flagK=False
        break
    idxK=ip.find('E',idxK+1)
    if idxK==-1 or idxK==lenip2-1:
        flagK=False
        break
    idxK=ip.find('A',idxK+1)
    break

if flagK and flagY:
    if idxK>idxY:
        print('YONSEI')
    else:
        print('KOREA')
elif flagK:
    print('KOREA')
else:
    print('YONSEI')