#１次元DPで持つと、同じ商品で、複数回入れるときに更新された値を確認できる前のものが更新されたときに
# 重さをインデックスに持つ。
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N,W = LI()
M = [[] for i in range(N)]
for i in range(N):
    M[i] = LI()

#一次元DPの回答

dp = [0]*(W+1)

for v,w in M:
    for i in range(W+1):
        if i>=w:
            dp[i] = max(dp[i-w]+v, dp[i])
print(dp[W])
#二次元DPの回答

dp = [[0]*(W+1) for i in range(N+1)]

for i in range(N):
    for w in range(W+1):
        A = range(w//M[i][1]+1)
        #for multi in range(w//M[i][1]+1):
        if w >= M[i][1]:
            dp[i+1][w] = max(dp[i][w],dp[i+1][w -M[i][1]] + M[i][0])
        else:
            dp[i+1][w] = max(dp[i+1][w], dp[i][w])

print(max(dp[N]))
#print(dp[N])