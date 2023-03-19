import sys

N=int(sys.stdin.readline())
S=set()
for _ in range(N):
	str_=sys.stdin.readline().rstrip()
	if str_[:3]=="add":
		if int(str_.split()[1]) not in S:
			S.add(int(str_.split()[1]))
	elif str_[:3]=="rem":
		if int(str_.split()[1]) in S:
			S.remove(int(str_.split()[1]))
	elif str_[:3]=="che":
		if int(str_.split()[1]) in S:
			print(1)
		else:
			print(0)
	elif str_[:3]=="tog":
		if int(str_.split()[1]) in S:
			S.remove(int(str_.split()[1]))
		else:
			S.add(int(str_.split()[1]))
	elif str_[:3]=="all":
		S=set(i for i in range(1,21))
	elif str_[:3]=="emp":
		S=set()