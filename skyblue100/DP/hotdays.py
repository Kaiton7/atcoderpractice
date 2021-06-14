def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
D,N = LI()

T = [II() for i in range(D)]
dic = {i:[] for i in range(61)}
data = []
for j in range(N):
    data.append(LI())
ware = [[] for i in range(D)]
for t in range(len(T)):
    for dx, da in enumerate(data):
        if da[0]<=T[t] and T[t]<=da[1]:
            ware[t].append(dx)

absc = [[0]*(N) for i in range(N)]

for i in range(N):
    for j in range(N):
        absc[i][j] = abs(data[i][2] - data[j][2])

DP = [[0]*N for i in range(D+1)]
for d in range(1, D):
    for i in ware[d-1]:
        for j in ware[d]:
            DP[d][j] = max(DP[d][j], DP[d-1][i] + absc[i][j])
print(max(DP[D-1]))


