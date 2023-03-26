st=input()
U=st.count('U')
D=st.count('D')
P=st.count('P')
C=st.count('C')
if (U==1 and D+P+C==0) or (C==1 and D+P+U==0):
    print('U',end='')
else:
    if not (P+D)%2:
        if (U+C)>(P+D)//2:
            print('U',end='')
    else:
        if (U+C)>(P+D)//2+1:
            print('U',end='')
    if P+D>0:
        print('D',end='')
        print('P',end='')