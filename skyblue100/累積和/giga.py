# L,Rという区間を二次元座標に圧縮？転換する
# 二次元のマスを見ればどの区間にどれが在るのか分かる、累積和
# Nが少ないのでできる

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
# マス目の価格の K 乗せても同じ
 
import numpy as np
 
H,W,K,V = map(int,readline().split())
A = np.zeros((H+1,W+1),np.int64)
A[1:,1:] = np.array(read().split(),np.int64).reshape(H,W) + K
print("AAmaspy",A)

Acum = np.cumsum(A,axis=0).cumsum(axis=1)
print(Acum)
opt_area = 0
for dx in range(1,H+1):
    # 列和を圧縮
    B = Acum[dx:] - Acum[:-dx]
    for C in B:
        can_buy_width = np.arange(W+1) - np.searchsorted(C,C-V)
        area = can_buy_width.max() * dx
        if opt_area < area:
            opt_area = area
 
print(opt_area)

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

R,C,K,V = LI()

#D = [LI() for _ in range(M)]
S = [[0]*(C+1) for i in range(R+1)]
#a = [[0]*(R+1) for i in range(C+1)]
A =[[0 for i in range(C+1)]]
for i in range(R):
    A.append([0]+LI())

for i in range(1,R+1):
    for j in range(1,C+1):
        S[i][j]= S[i-1][j]+S[i][j-1]-S[i-1][j-1] +A[i][j]

res = 0
for r1 in range(1,R+1):
    r1 = r1-1
    for c1 in range(1,C+1):
        c1 = c1-1

        for r2 in range(r1,R+1):
            for c2 in range(c1, C+1):
                #print(p,q)
                
                #print(S[q][q], S[q][p] , S[p][q] , S[p][p]
                B = (r2-r1)*(c2-c1)
                tmp = K*B + S[r2][c2] - S[r2][c1] - S[r1][c2] + S[r1][c1]
                if V>=tmp:
                    res = max(res, B)


print(res)