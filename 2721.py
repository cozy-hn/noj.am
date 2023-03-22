for _ in range(int(input())):
    print(sum([i*(i+2)*(i+1)//2 for i in range(1,int(input())+1)]))