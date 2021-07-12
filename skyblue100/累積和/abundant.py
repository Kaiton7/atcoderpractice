
def chkprint(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))


def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = 10**10

N = II()
A = LI()
S = [0]*(N+1)
for ai in range(len(A)):
    S[ai+1] = A[ai] + S[ai]

#print(S)
for k in range(1,N+1):
    ans = 0
    for i in range(N-k+1):
        #print(i+k,i)
        ans = max(ans, S[i+k]- S[i])
    print(ans)
