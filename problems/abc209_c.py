from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
def chkprint(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

N = II()
C = LI()

MOD = 10**9+7
ans = 0
C.sort()
#print(C)
pattern = 1
for ix, c in enumerate(C):
    
    #ans+= pattern*c -(ix*pattern)
    pattern = (pattern*c - (ix*pattern))%MOD
    #print(pattern)
print(pattern)

