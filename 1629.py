def power(a,b,c):
    if b==1:
        return a%c
    if b%2:
        return ((power(((a%c)*(a%c))%c,b//2,c)%c)*(a%c))%c
    else:
        return power(((a%c)*(a%c))%c,b//2,c)%c
a,b,c=map(int,input().split())
print(power(a,b,c))