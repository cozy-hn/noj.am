import sys
input=lambda: sys.stdin.readline().rstrip()
timeset=set()
for i in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']:
    for j in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']:
        for k in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']:
            timeset.add(i+','+j+','+k)
for i in range(sum(map(int,input().split()))):
    h,m,s=input().split(':')
    h=int(h)
    h=str(h)
    m=int(m)
    m=str(m)
    s=int(s)
    s=str(s)
    for i in range(40):
        if int(s)==60:
            s='0'
            m=str(int(m)+1)
        if int(m)==60:
            m='0'
            h=str(int(h)+1)
        if int(h)==24:
            break
        if h+','+m+','+s in timeset:
            timeset.remove(h+','+m+','+s)
        s=str(int(s)+1)
print(len(timeset))