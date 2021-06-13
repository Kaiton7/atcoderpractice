#１次元DPで持つと、同じ商品で、複数回入れるときに更新された値を確認できる前のものが更新されたときに
# 重さをインデックスに持つ。
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N,W = LI()
M = [[] for i in range(N)]
C = LI()
#一次元DPの回答

dp = [10**9]*(N+1)
dp[0] = 0
for c in C:
    #print(c,dp)
    for i in range(c,N+1):
        #print(i)
        dp[i] = min(dp[i-c]+1, dp[i])
print(dp[N])
