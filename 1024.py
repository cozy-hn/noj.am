a,b=map(int,input().split())
while True:
    if a%b==0 and b%2==1:
        if a//b-b//2>=0:
            for i in range(b-1):
                print(a//b-b//2+i, end=' ')
            print(a//b-b//2+b-1)
            break
    if a%b==b//2 and b%2==0:
        if a//b-b//2+1>=0:
            for i in range(b-1):
                print(a//b-b//2+1+i, end=' ')
            print(a//b-b//2+1+b-1)
            break
    if b>99:
        print(-1)
        break
    b+=1