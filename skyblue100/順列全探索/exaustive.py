from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe


def LI():
    return list(map(int, input().split()))

def II():
    return int(input())

def chkprint(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))


N = II()
A = LI()
Q = II()
M = LI()
Ms = set(M)
PP  = set()
for i in range(1<<N):
    ans = 0
    j= 0
    while i > 0:
        if i&1==1:
            ans+=A[j]
        i>>=1
        j+=1
    if ans in Ms:
        PP.add(ans)
for m in M:
    if m in PP:
        print("yes")
    else:
        print("no")






