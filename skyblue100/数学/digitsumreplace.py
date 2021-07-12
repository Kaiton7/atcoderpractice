def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
M= II()
S =0
D = 0
for i in range(M):
    t =LI()
    S+=t[0]*t[1]
    D+=t[1]
print(D-1+(S-1)//9)


"""
res = []
def lc(p,c,bt):
    global res
    c+=1
    if len(p)<=2 and int(p[0])+int(p[1])<10:

        res.append([p,c,bt])
    else:
        for i in range(len(p)-1):
            t = int(p[i])+int((p[i+1]))
            p_ = p[:i]+str(t)+p[i+2:]
            at= bt + [p]
            lc(p_, c, at)
import random
ra = random.randint(100000,999999)
lc(str(ra), 0, [])
print(ra)
for r in range(1,len(res)):
    if res[r-1][1]!=res[r][1]:
        print("widhgs")
        print(res)
print("all",res[0],res[1])
print("length", len(res))
print("ra",ra)
"""