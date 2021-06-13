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
for _ in range(N):
    X = input()
    Y = input()
    #DP = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
    DP1 = [0]*(len(Y)+1)
    DP2 = [0]*(len(Y)+1)
    #print(DP)
    for ix in range(1,len(X)+1):
        for iy in range(1,len(Y)+1):
            if X[ix-1]==Y[iy-1]:
                #print(ix,iy)
                #DP[ix][iy] = DP[ix-1][iy-1]+1
                DP2[iy] = DP1[iy-1]+1
            else:
                #DP[ix][iy] = max(DP[ix-1][iy],DP[ix][iy-1])
                DP2[iy] = max(DP1[iy],DP2[iy-1])
        DP1,DP2 = DP2,DP1
    print(DP1[len(Y)])
                           

            