# 計算量を減らしたダイクストラを実装

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = 10**10

import collections, heapq
class Dijkstra():
    def __init__(self) -> None:
        self.e = collections.defaultdict(list)
    
    def add(self, u, v, d):
        self.e[u].append([v,d])
        self.e[v].append([u,d])
    
    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] !=v]
        self.e[v] = [_ for _ in self.e[v] if _[0] !=u]

    def search(self, s):
        d = collections.defaultdict(lambda:INF)
        d[s] = 0
        q = []
        heapq.heappush(q, (0,s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True
            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv]>vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))
        return max(d.values())

def main():
    N,M = LI()
    dk = Dijkstra()
    for _ in range(M):
        a,b,t = LI()
        dk.add(a,b,t)
    r = [dk.search(i) for i in range(1, N+1)]
    return min(r)
print(main())

    

"""
ve, ee = LI()
distlist = [[INF]*ve for _ in range(ve)]
negativecycle = False
for _ in range(ee):
    s,t,dist= LI()
    s,t = s-1,t-1
    distlist[s][t]  = dist
    distlist[t][s] = dist
for v in range(ve):
    distlist[v][v] = 0

for k in range(ve):
    for i in range(ve):
        for j in range(ve):
            if distlist[i][k]!=INF and distlist[k][j]!=INF:
                if distlist[i][j] > distlist[i][k] + distlist[k][j]:
                    distlist[i][j]  = distlist[i][k] + distlist[k][j]
res = INF
for ix,lst in enumerate(distlist):
    t = 0
    for i in lst:
        if i==INF:
            pass
        else:
            t += i
    if t<res:
        ans = ix
    res = min(res,t)

print(max(distlist[ans]))


"""