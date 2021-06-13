
# 3日連続で食べれない時は2回連続までデータを保持する
# 食べれるものが決まっている日は、それだけしか食べれないというより
# 他のものを食べれないというふうに考えて、フラグを立てておく
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N,K = LI()

# dp[i][j][k]:i日目、j番目のパスタを食べるとき、k連続で食べたとき
DP = [[[0,0],[0,0],[0,0]] for i in range(N)]
# strike[i][j] i日目j番目のパスタを食べれるかどうか
strike = [[True,True,True] for i in range(N)]
for k in range(K):
    i, j = LI()
    strike[i-1][j-1] = False
    strike[i-1][j-2] = False

for i in range(N):
    for j in range(3):
        if strike[i][j]:
            if i==0:
                DP[i][j][0] = 1
            else:
                DP[i][j][0] += DP[i-1][j-1][1] +DP[i-1][j-1][0] +DP[i-1][j-2][1] +\
                    DP[i-1][j-2][0]
                DP[i][j][1] += DP[i-1][j][0]
            DP[i][j][1]%=10000
            DP[i][j][1]%=10000
print(sum(map(sum, DP[-1]))%10000)