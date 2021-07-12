def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
eo = []
odd = []
for i in range(182):
    dd = int(i*(i+1)*(i+2)/6)
    eo.append(dd)
    if dd%2!=0:
        odd.append(dd)
DP = [10**12 for i in range(10**6+1)]
DP[0] = 0
DPd = [10**13  for i in range(10**6+1)]
DPd[0] = 0
for i in range(10**6+1):
    for ix, d in enumerate(eo):
        if i >= d:
            DP[i] = min(DP[i-d]+1, DP[i])
    for ixx, dd in enumerate(odd):
        if i >=dd:
            DPd[i] = min(DPd[i-dd]+1, DPd[i])
while True:
    N = II()
    if N==0:
        break
    print(DP[N],DPd[N])
        