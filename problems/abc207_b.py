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



A,B,C,D = LI()
E = C
A+=B
W = B//C
#chkprint(W,D)
if B//C >=D:
    print(-1)
else:
    c = 1
    X = A/E
    #chkprint(A,E,X,D)
    while A/E > D:
        X = A/E
        #chkprint(A,E,X,D)
        A+=B
        E+=C
        c+=1
    print(c)