from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe
from collections import defaultdict
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = float("inf")
#INF = 10**12
MOD = 10**4+7
N = II()
SD = {"J":0, "O":1, "I":2}
S = input()

dp = [[0]*8 for _ in range(N)]

#JOIの順でbitを割り振る

fr = 4

for i in range(N):
    # i番目の責任者
    si = SD[S[i]]
    if i==0:
        for b in range(1, 1<<3):
            #print(b)
            #print(b>>0&1, b>>si&1, )
            if (b>>0)&1 and (b>>si)&1:
                dp[i][b] = 1
        #print(dp)
    # 8パターン列挙する(正確には0人は省くので7パターン)
    for r in range(1, 1<<3):
        # 試しているパターンに責任者が含まれていないとこのループはパス
        if (r>>si)&1!=1:
            continue
        # 1つ前のパターンについて
        for ar in range(1, 1<<3):
            if ar & r ==0:
                continue
            dp[i][r]+=dp[i-1][ar]%MOD

print(sum(dp[N-1])%MOD)