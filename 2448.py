N=int(input())
star=[[" ", " ", "*", " ", " "],[" ", "*", " ", "*", " "],["*", "*", "*", "*", "*"]]
repeat=3
def printstar(N,star):
    global repeat
    if N==3:
        for i in range(len(star)):
            print(*star[i],sep="")
    else:
        for i in range(len(star)):
            star.append(star[i]+[" "]+star[i])
        for i in range(len(star)//2):
            star[i]=[" "*(repeat)]+star[i]+[" "*(repeat)]
        repeat*=2
        printstar(N//2,star)


printstar(N,star)