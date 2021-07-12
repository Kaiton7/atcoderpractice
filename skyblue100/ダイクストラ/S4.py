# Single Source Shortest Path
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

V,E,r = LI()

D = [[] for i in range(V)]
for i in range(E):
    s,t,d = LI()
    D[s].append([t,d])


from collections import deque

Q = deque(D[r])
P_f = [10**9 for i in range(V)]
P_f[r] = 0
while Q:
    t,r_t = Q.popleft()
    if r_t < P_f[t]:
        P_f[t] = r_t
        for d in D[t]:
            Q.append([d[0],d[1]+r_t])

for p in P_f:
    if p==10**9:
        print("INF")
    else:
        print(p)



