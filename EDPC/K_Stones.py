from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())


N,K = LI()
A = LI()


dp = [False]*(110000)
#dp = [False]*(8)

for i in range(1,K+1):
    for j in range(N):
        if i-A[j]>=0:
            dp[i] |= not dp[i-A[j]]
            #print("K",i,"A",A[j])
            #print(dp)
if dp[K]:
    print("First")
else:
    print('Second')