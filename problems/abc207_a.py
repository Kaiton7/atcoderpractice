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

A = LI()
A.sort()
print(A[2]+A[1])



