def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()

A = LI()

A = [i+1 for i in A]

C = [0 for i in range(len(A)+10)]
C[0] = 3

res = 1
MOD = 10**9+7
for a in A:
    if C[a-1] == 0:
        print(0)
        exit()
    else:
        res=res*(C[a-1]-C[a])%MOD
        C[a]+=1
print(res)
    