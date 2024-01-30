def boyer(P,T):
    if len(P)>len(T):
        return -1
    m=len(P)
    i=j=m-1
    while i<len(T):
        if P[j] == T[i]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            i += m - min(j, 1 + last_oc(T[i+1],P))
            j = m - 1
    return -1
    

def last_oc(ki_tu,P):
    for i in range(0,len(P)):
        if ki_tu == P[i]:
            return i
    return -1