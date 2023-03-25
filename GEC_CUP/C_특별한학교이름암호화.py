from string import ascii_lowercase  
alpha = list(ascii_lowercase)
li=['northlondo','branksomeh','koreainter','stjohnsbur']
dic={'northlondo':'NLCS','branksomeh':'BHA','koreainter':'KIS','stjohnsbur':'SJA'}
ip=input()
while True:
    move=1
    if ip in li:
        print(dic[ip])
        break
    else:
        k=0
        ipli=list(ip)
        for i in ipli:
            index = alpha.index(i)
            ipli[k]=alpha[(index-move)%26]
            k+=1
        ip=''.join(ipli)
        move+=1