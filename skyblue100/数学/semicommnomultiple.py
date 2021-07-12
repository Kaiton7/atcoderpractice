def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
    
from math import gcd
def arraylcm(a):
    lcm = 1
    for i in a:
        lcm = lcm*i//gcd(lcm, i)
    return lcm
N,M= LI()
A = LI()
A = [i//2 for i in A]
while A[0]%2==0:
    for i in range(len(A)):
        if A[i]%2!=0:
            print(0)
            exit()
        A[i]//=2
    M//=2

for i in range(len(A)):
    if A[i]%2==0:
        print(0)
        exit()


lcm = arraylcm(A)
res  = int((M//lcm+1)//2)

print(res)