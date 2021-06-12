N,M = map(int,input().split())
L = [int(input()) for i in range(N)]
L = L+[0]
Q = [a+b for i, a in enumerate(L) for b in L[i:]]
Q.sort()
from bisect import bisect

Q = Q[:bisect(Q,M)]
ans = -1
for q in Q:
    i = bisect(Q, M-q)
    ans = max(q+Q[i-1], ans)
print(ans)


