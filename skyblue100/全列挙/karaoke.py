from sys import stdin
from itertools import combinations
 
input = stdin.readline

N,M = map(int, input().split())
A = [[] for i in range(N)]
for n in range(N):
    A[n] = list(map(int, input().split()))
print(A)
comb = combinations([i for i in range(M)], 2)
t = 0
for i in list(comb):
    print(i)
    tmp  = 0

    for a in A:
        tmp+= max(a[i[0]], a[i[1]])
    t = max(t, tmp)   
print(t)