def CCW(a,b,c,d): #vector ab, cd
    if a*d-c*b > 0:
        return 1
    elif a*d-c*b < 0:
        return -1
    else:
        return 0