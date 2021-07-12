# Single Source Shortest Path

#だめな街はsetで管理すると無駄な探索を防げる

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
from collections import deque
N,M,K,S = LI()
pp,qq = LI()
Danger = [0 for i in range(N)]
Edge = [[] for i in range(N)]
C = []
for i in range(K):
    c = II()
    c = c-1
    Danger[c] = -1
    C.append(c)
for i in range(M):
    a,b = LI()
    a,b = a-1,b-1
    Edge[a].append(b)
    Edge[b].append(a)

Q = deque()
for c in C:
    count = 0
    Q.append([c,count+1])
    while Q:
        c,count = Q.popleft()
        for ns in Edge[c]:
            if count <= S:
                Q.append([ns,count+1])
                Danger[ns] = 1
for c in C:
    Danger[c] =-1


def dks(s,g,D,N,Danger):
    P_f = [10**9 for i in range(N)]
    Q = deque([[s,0]])
    P_f[s] = 0
    #print(D)
    while Q:
        #print(Q)
        t,r_t = Q.popleft()
        #print(t,r_t)
        for d in D[t]:
            if Danger[d]==-1:
                continue
            elif Danger[d]==1:
                if r_t+qq < P_f[d]:
                    P_f[d] = r_t+qq
                    Q.append([d,r_t+qq])
            else:
                if r_t+pp < P_f[d]:
                    P_f[d] = r_t+pp
                    Q.append([d,r_t+pp])
    #print(P_f)
    if Danger[N-1]:
        return P_f[N-1]-qq
    else:
        return P_f[N-1]-pp

print(dks(0,N-1,Edge, N,Danger))

