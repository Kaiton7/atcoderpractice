from collections import deque
from heapq import heappush, heappop
from inspect import currentframe

def chkprint(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))


def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = 10**10
N = II()
Ed = [[] for j in range(N+1)]
order = []
root = 1
MOD = 10 ** 9 + 7


#print(Ed)
for i in range(N-1):
    a,b = LI()
    Ed[a].append(b)
    Ed[b].append(a)


Q = deque([[root,0]])
parent = [-1]*(N+1)
while Q:
    chkprint(Q)
    #a = Q.popleft()
    #print(a)
    t,p= Q.popleft()
    if parent[t]!=-1:
        continue
    parent[t] = p
    order.append(t)
    for nx in Ed[t]:
        if parent[nx]!=-1:
            continue
        Q.append([nx,t])

chkprint(order,parent,Ed)

x = (MOD + 1) // 2
power = [1] * (N+100)
power_inv = [1] * (N+100)
for i in range(1,N+100):
    power[i] = power[i-1] * 2 % MOD
    power_inv[i] = power_inv[i-1] * x % MOD

chkprint(power,power_inv)