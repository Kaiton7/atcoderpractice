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

N = int(input())
A = list(map(int,input().split()))
sum_ = [0]*(N+1)
for i in range(N):
    sum_[i+1] = sum_[i]+A[i]
mem = [[0]*(N+1) for i in range(N+1)]
dp = [[0]*(N+1) for i in range(N+1)]
mem[0][0] = 1
mod = int(1e9+7)

for i in range(1,N+1):
    for k in range(1,N+1):
        dp[i][k] = mem[k-1][sum_[i]%k]
    for k in range(1,N):
        mem[k][sum_[i]%(k+1)] += dp[i][k]
        mem[k][sum_[i]%(k+1)]%=mod
      

    #chkprint(dp)
#print(sum_)
#print(mem)
ans = sum(dp[N])%mod
print(ans)
