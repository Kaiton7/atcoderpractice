def LI():
    return list(map(int, input().split()))
def II():
    return int(input())



N,W = LI()
M = [[] for i in range(N)]
for i in range(N):
    M[i] = LI()

dp = [[0]*(W+1) for i in range(N)]
for j in range(M[0][1],W+1):
    dp[0][j] = M[0][0]
for i in range(1,N):
    for w in range(W+1):
        if w >= M[i][1]:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-M[i][1]] + M[i][0])
        else:
            dp[i][w] = dp[i-1][w]

#print(dp)
print(max(dp[N-1]))






