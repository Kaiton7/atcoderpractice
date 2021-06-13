#LCS
# dp[i][j]:各文字列をi,j番目まで見たときのLCSを入れる
# dp[i][j]が一致するとき、というか一致しているとみなす時は
# dp[i-1][j-1]からしか遷移できない。dp[i][j-1]やその逆は既にi,jを使ってしまっているから
# 逆に、i,jを一致しているとしないときは、dp[i][j-1]から飛んでこれる
# 一次元DPでやる時は、i文字目を見ているときに、j文字目を使っている場合と、j-1文字目までの場合でにパターンある

# ###
# #&#
# ###
# &の箇所で左と左上の2パターンある
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N= II()

X  =LI()

DP = [[0]*(21) for _ in range(N-1)]

DP[0][X[0]] = 1
for ix, x in enumerate(X[1:-1]):
#    print(ix,x)
    for idp, dp in enumerate(DP[ix]):
        if dp>0:
            nxplus = idp+x
            nxminus = idp-x
            if nxplus >= 0 and nxplus <=20:
                DP[ix+1][nxplus]+=dp
            if nxminus >= 0 and nxminus <=20:
                DP[ix+1][nxminus]+=dp
    #print(idp,dp)
print(DP[len(X)-2][X[-1]])
