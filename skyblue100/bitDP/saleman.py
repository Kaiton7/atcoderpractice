V, E = map(int, input().split())
INF = 10**10
cost = [[INF]*V for _ in range(V)] # 重み
for e in range(E):
    s, t, d = map(int,input().split())
    cost[s][t] = d

dp = [[-1] * V for _ in range(1<<V)] # dp[S][v]
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe

def chkprint(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

def dfs(S, v, dp):
    if dp[S][v]!=-1:
        return dp[S][v]
    # 返ってきたとき
    if S==(1<<V)-1 and v==0:
        return 0
    res = INF
    for nxv in range(len(cost[v])):
        if cost[v][nxv]==INF or S&(1<<nxv)!=0:
            continue
        chkprint(v,nxv)
        res = min(res, dfs(S|(1<<nxv),nxv, dp)+cost[v][nxv])
    #exit()
    dp[S][v]=res
    return res
ans = dfs(0, 0, dp) # 頂点0からスタートする。ただし頂点0は未訪問とする
if ans == INF:
    print(-1)
else:
    print (ans)