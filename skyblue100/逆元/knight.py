def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

X,Y = LI()
MAX = 5100000

MOD = 1000000007

fac, finv, inv = [0 for i in range(MAX)],[0 for i in range(MAX)],[0 for i in range(MAX)]

def cominit():
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1,1
    inv[1] = 1
    for i  in range(2,MAX):
        fac[i] = fac[i-1] * i %MOD
        inv[i]  =MOD - inv[MOD%i]*(MOD//i)%MOD
        finv[i] = finv[i-1] * inv[i] %MOD

def COM(n:int, k:int):
    if n< k:
        return 0

    if n <0 or k <0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD
cominit()
b = (2*X-Y)/3
a = X-2*(2*X-Y)/3
if b==((2*X-Y)//3) and a==(X-2*(2*X-Y)//3):
    print(COM(int(a+b),int(a)))
else:
    print(0)
