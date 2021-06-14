def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N,M = LI()

D = [0]+[II() for i in range(N)]
C = [0]+[II() for i in range(M)]

DP = [[10**9]*(M-N+1) for i in range(N)]

for i in range(M-N+1):
    DP[0][i] = D[0]*C[i]
for n in range(1,N):
    for m in range(M-N+1):
        for mm in range(m+1):
            DP[n][m] = min(DP[n][m],DP[n-1][mm]+D[n]*C[n+mm])
print(min(DP[N-1]))

