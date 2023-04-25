for _ in range(int(input())):
    STR=input()
    print(STR[0],end='')
    for i in range(1,len(STR)):
        if STR[i]!=STR[i-1]:
            print(STR[i],end='')
    else:
        print()