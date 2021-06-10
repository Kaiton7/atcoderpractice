import itertools
N =  int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

#N = 100
data = [0]*(N+1)
def add(k, x):
    while k<=N:
        data[k]+=x
        k+=k&-k
def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k&-k
    return s

ans_s = 0
ans_c = 0
fact = [1]*(N+1)
for i in range(1,N+1):
    fact[i] = i*fact[i-1]

def calcorder(X):
    ans = 0
    for ix, x in enumerate(X):
        ans += ((x-1)-get(x))*fact[N-1-ix]
        add(x,1)
    ans+=1
    return ans
ans_s = calcorder(P)
data = [0]*(N+1)
ans_c = calcorder(Q)

#print(ans_s,ans_c,fact)
print(abs(ans_s - ans_c))

