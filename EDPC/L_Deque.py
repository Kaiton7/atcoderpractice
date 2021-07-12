from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()
A = LI()

dp = [[0]*(N+1) for i in range(N+1)]

# Nが奇数のとき最後が太郎
# dp[i][i] 最後まで取ったとき。
# dp[i][i+1] iだけ残っている数列
# もらうDP??
# i,jのときに、i-1,j からa[i] をもらうのか、i,j-1からa[j]をもらうのか
# どちらがいいのかな。

for Length  in range(1,N+1):
    i = 0
    while i+Length <= N:
        j = i+Length
        #先手
        if (N-Length)%2==0:
            dp[i][j] = max(dp[i+1][j] + A[i], dp[i][j-1] + A[j-1])
        else:
            dp[i][j] = min(dp[i+1][j] - A[i], dp[i][j-1] - A[j-1])

        i+=1
print(dp[0][N])




"""
X,Y = 0
for i in range(N):
    j=i
    while (j-i)<(N-1):
        # 全体から区間を引いたときに2で割り切れるとき、先手：太郎
        if (N-(j-i))%2==0:
            if abs(X-(Y+A[i-1])) < abs(X-(Y+A[j+1])):
                i-=1
                Y+=A[i]
            else:
                j+=1
                Y+=A[j]
        else:
            if abs(Y-(X+A[i-1])) < abs(Y-(X+A[j+1])):
                j+=1
                X+=A[j]
            else:
                i-=1
                Y+=A[i]
"""

