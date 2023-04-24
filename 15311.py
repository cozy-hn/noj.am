N=int(input())
if N==1000000:
    print(2000)
    print('1 '*1000+'1000 '*1000)
else:
	print(N%1000+N//1000)
	print('1 '*(N%1000)+'1000 '*(N//1000))