# L,Rという区間を二次元座標に圧縮？転換する
# 二次元のマスを見ればどの区間にどれが在るのか分かる、累積和
# Nが少ないのでできる


def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N,M,Q = LI()

#D = [LI() for _ in range(M)]
S = [[0]*(N+2) for i in range(N+2)]
a = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    l,r = LI()
    a[l][r]+=1
    
for i in range(1,N+1):
    for j in range(1,N+1):
        S[i][j]= S[i-1][j]+S[i][j-1]-S[i-1][j-1] +a[i][j]
for _ in range(Q):
    p,q = LI()
    #print(p,q)
    p = p-1
    q = q
    #print(S[q][q], S[q][p] , S[p][q] , S[p][p])

    print(S[q][q] - S[q][p] - S[p][q] + S[p][p])
