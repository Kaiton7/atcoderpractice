def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
from itertools import accumulate

N,Q = LI()
A = LI()
C = [1]+LI()+[1]
D = [0 for i in range(N+1)]
mod = 1000000007

for ia in range(len(A)-1):
    D[ia+1] = pow(A[ia],A[ia+1],mod)
res = 0
#print(D,C)
acc = list(accumulate(D))
for ic in range(len(C)-1):
    res+=abs(acc[C[ic+1]-1] - acc[C[ic]-1])%mod

print(res%mod)