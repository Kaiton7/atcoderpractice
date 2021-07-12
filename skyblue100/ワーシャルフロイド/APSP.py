
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = 10**10
ve, ee = LI()
distlist = [[INF]*ve for _ in range(ve)]
negativecycle = False
for _ in range(ee):
    s,t,dist= LI()
    distlist[s][t]  = dist
for v in range(ve):
    distlist[v][v] = 0

for k in range(ve):
    for i in range(ve):
        for j in range(ve):
            if distlist[i][k]!=INF and distlist[k][j]!=INF:
                if distlist[i][j] > distlist[i][k] + distlist[k][j]:
                    distlist[i][j]  = distlist[i][k] + distlist[k][j]

for v in range(ve):
    if distlist[v][v]<0:
        negativecycle  = True

if negativecycle:
    print("NEGATIVE CYCLE")
else:
    for lst in distlist:
        put = ""
        for i in lst:
            if i==INF:
                put+="INF"+" "
            else:
                put+=str(i) +" "
        print(put.rstrip())


