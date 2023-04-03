import sys
input=lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    money=int(input())
    print(money//25,(money%25)//10,(money%25%10)//5,(money%25%10%5)//1)