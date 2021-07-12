# Single Source Shortest Path
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N,K = LI()
D = [[] for i in range(N)]
from collections import deque
def dks(s,g,D,N):
    P_f = [10**9 for i in range(N)]
    Q = deque(D[s])
    P_f[s] = 0
    while Q:
        t,r_t = Q.popleft()
        if r_t < P_f[t]:
            P_f[t] = r_t
            for d in D[t]:
                Q.append([d[0],d[1]+r_t])
    
    if P_f[g]==10**9:
        return -1
    else:
        return P_f[g]
for _ in range(K):
    f = LI()
    if f[0]==1:
        #print("len(D)",len(D),"f",f)
        D[f[1]-1].append([f[2]-1,f[3]])
        D[f[2]-1].append([f[1]-1,f[3]])    
    else:
        print(dks(f[1]-1,f[2]-1,D,N))
