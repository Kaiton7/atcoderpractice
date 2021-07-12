# numpyのcumsumを使う
# 半開区間ということを忘れずに二次元累積和を使う

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())


R,C = LI()
K = II()

field = [input() for i in range(R)]
SJun = [[0]*(C+1) for i in range(R+1)]
SIce = [[0]*(C+1) for i in range(R+1)]
SOce = [[0]*(C+1) for i in range(R+1)]

for r in range(R):
    for c in range(C):
        SJun[r+1][c+1] = SJun[r][c+1] + SJun[r+1][c] - SJun[r][c] + field[r][c].count("J")
        SIce[r+1][c+1] = SIce[r][c+1] + SIce[r+1][c] - SIce[r][c] + field[r][c].count("I")
        SOce[r+1][c+1] = SOce[r][c+1] + SOce[r+1][c] - SOce[r][c] + field[r][c].count("O")

def pp(F,r1,c1, r2,c2 ):
    return(F[r2][c2]-F[r1][c2]-F[r2][c1] + F[r1][c1])
for k in range(K):
    r1,c1, r2,c2 = LI()
    r1,c1, r2,c2 = r1-1,c1-1, r2,c2
    #print(r1,c1, r2,c2)
    print(pp(SJun,r1,c1, r2,c2),pp(SOce,r1,c1, r2,c2),pp(SIce,r1,c1, r2,c2))
