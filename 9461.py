for _ in range(int(input())):
    a=b=c=1
    for _ in range(int(input())-1):
        a,b,c=b,c,a+b
    print(a)