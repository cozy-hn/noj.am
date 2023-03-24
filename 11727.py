a=b=1
for _ in range(int(input())):
    a,b=b,a*2+b
print(a%10007)