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

N,M = map(int, input().split())

TE = [[INF]*(N) for _ in range(N)]
cost = [[INF]*(N) for _ in range(N)] 
dp = [[[-1, 0] for j in range(N)] for i in range(1<<N)]

for i in range(M):
    s,t,d,time = map(int, input().split())
    TE[s-1][t-1] = time
    TE[t-1][s-1] = time

    cost[s-1][t-1] = d
    cost[t-1][s-1] = d

def salesman(S, v):
    # dpに入れる値でINFを使っている
    # もともとの値をINFにしてそれで判定すると
    # 訪問したのに未訪問になり、同じパスを何度も探索する必要が出てくる
    if dp[S][v][0]>0:
        return dp[S][v]
    if S == (1<<N)-1 and v == 0:
        dp[S][v][0] = 0
        dp[S][v][1] = 1
        return [0,1]
    ans = INF
    rc = 0
    for nv in range(N):
        if not S>>nv&1:
 
            time=TE[v][nv]
            tp, tc = salesman(S|(1<<nv),nv)
            np = tp+cost[v][nv]
            if np <= time:
                if np < ans:
                    ans = np
                    rc = tc
                elif np==ans:
                    rc+=tc
    dp[S][v][0] = ans
    dp[S][v][1] = rc
    return [ans, rc]
mp,rr = salesman(0, 0)

if mp==INF:
    print("IMPOSSIBLE")
else:
    print(mp, rr)