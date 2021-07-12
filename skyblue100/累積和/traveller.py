def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
from itertools import accumulate


N,C = LI()
D = [II() for i in range(N-1)]
DA = [0]+list(accumulate(D))
Q = [II() for i in range(C)]

cl = 0
#print(DA)
res = 0
for q in Q:
    q_ = cl+q
    #print("cl,q,DA",cl,q,DA)
    res += abs(DA[cl]-DA[q_])%100000
    #print(res,q_,DA)
    cl+=q
print(res%100000)

