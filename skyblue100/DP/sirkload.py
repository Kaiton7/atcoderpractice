def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N,M = LI()

D = [0]+[II() for i in range(N)]
C = [0]+[II() for i in range(M)]

DP = [[0]*(M+1)] +[[10**9]*(M+1) for i in range(N)]
for i in range(1,N+1):
    for j in range(1,M+1):
        DP[i][j] = min(DP[i][j-1], DP[i-1][j-1] + D[i]*C[j])
print(DP)
print(DP[N][M])

