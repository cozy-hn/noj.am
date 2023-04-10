수로,미로,장애물=sorted(map(int,input().split()))
if 장애물>=수로+미로:
    print(2*(수로+미로)-1)
else:
    print(수로+미로+장애물)