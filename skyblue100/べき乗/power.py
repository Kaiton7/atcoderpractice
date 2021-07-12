def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

m,n = LI()
m_ = 1
mod = 1000000007

import math
#m = math.sqrt(m)
while n>0:
    #print(n,bin(n),m_,m)
    if n&1:
        m_ = m_*m%mod
    m = m**2%mod
    n>>=1
print(m_)
