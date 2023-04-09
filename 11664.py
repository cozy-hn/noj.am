x1,y1,z1,x2,y2,z2,x3,y3,z3 = map(int,input().split())

def dis(x1,y1,z1,x2,y2,z2):
	return ((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5

def ang(v1,v2,v3,v4,v5,v6):
	if (v1*v4+v2*v5+v3*v6)>=0:
		return 1
	else:
		return -1

def det(v1,v2,v3,v4,v5,v6):
    return ((v2*v6-v3*v5)**2+(v3*v4-v1*v6)**2+(v1*v5-v2*v4)**2)**0.5

if ang(x2-x1,y2-y1,z2-z1,x3-x1,y3-y1,z3-z1)<0:
    print(dis(x1,y1,z1,x3,y3,z3))
elif ang(x1-x2,y1-y2,z1-z2,x3-x2,y3-y2,z3-z2)<0:
	print(dis(x2,y2,z2,x3,y3,z3))
else:
    print(abs(det(x2-x1,y2-y1,z2-z1,x3-x1,y3-y1,z3-z1))/dis(x1,y1,z1,x2,y2,z2))