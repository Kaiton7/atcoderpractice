def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()
S = LI()
Q = II()
T = LI()

cnt = 0

def BS(t,l=-1,r=len(S)):
    #print(t,l,r)
    while abs(l-r)>1:
        m = (l+r)//2
        if S[m]>t:
            r = m
            return BS(t, l, r)
        elif S[m]<t:
            l = m
            return BS(t,l,r)
        else:
            return True
    return False


for t in T:
    if BS(t):
        cnt+=1
print(cnt)