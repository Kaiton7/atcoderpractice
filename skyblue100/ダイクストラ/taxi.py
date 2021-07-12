#考え方だけ充てて
# 実装は答え見た
# heapqは普通のリストにheappushを使ってもヒープにしてくれるっぽい
# コストの増減の単位ごとの遷移で行けるところはどこか考える
# 
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

from collections import deque
from heapq import heappop, heappush
N,K = LI()
CR = []
for i in range(N):
    c,r = LI()
    CR.append([c,r])
Edge = [[] for i in range(N)]
for i in range(K):
    a,b = LI()
    a,b = a-1,b-1
    Edge[a].append(b)
    Edge[b].append(a)

INF = 10**10

def bfs(s):
    Q = deque([s])
    dist = [INF]*N
    dist[s] = 0
    while Q:
        v = Q.popleft()
        for w in Edge[v]:
            if dist[w]!=INF:
                continue
            dist[w] = dist[v]+1
            Q.append(w)
    return dist

dist_mat = [bfs(s) for s in range(N)]
for i in range(N):
    c,r = CR[i]
    for j in range(N):
        dist_mat[i][j] = c if dist_mat[i][j] <= r else INF
    
q = [(0,0)]
dist=[INF]*N
#dist[0] = 0
while q:
    dv, v = heappop(q)
    if dv >dist[v]:
        continue
    if v==N-1:
        break

    # 繋がっているところならどこでも一回で遷移できる
    # edgeだけじゃなくて全てのnodeを対象に探索する
    for w in range(N):
        dw = dv +dist_mat[v][w]
        if dw >= dist[w]:
            continue
        dist[w] = dw
        heappush(q,(dw,w))
print(dist[N-1])
