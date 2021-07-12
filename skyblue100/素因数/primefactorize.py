def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()

import math
Q = []
n = 2
nc = N
while n <= int(math.sqrt(N)):
    if N%n==0:
        N//=n
        Q.append(str(n))
    else:
        n+=1
#残った数が素数ならnが1になっていないよ
if n!=1:
    Q.append(str(N))

print(str(nc) + ": " + " ".join(Q))
