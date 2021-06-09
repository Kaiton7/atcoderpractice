class SegmentTree:
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.data=  [default]*(self.size*2)
        self.f = f
    
    def update(self, ix, x):
        ix += self.size
        self.data[ix]+=x
        while ix>0:
            ix>>=1
            self.data[ix] = self.f(self.data[2*ix], self.data[2*ix+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        #print(l,r,self.data,self.size)
        lres, rres = self.default, self.default
        while l<r:
            if l&1:
                lres = self.f(lres, self.data[l])
                l+=1
            # 半壊区間なのでrが基数のとき上を飛ばしてすぐ左に動く
            if r&1:
                r-=1
                rres  = self.f(self.data[r], rres)

            l >>= 1
            r >>= 1
        #lとrに幅が無くなったら、区間全てを確認したことになるので
        # それを足す
        res = self.f(lres, rres)
        return res



N = int(input())
#Nfact = [0]*(N+1)
import random
A = list(map(int, input().split()))
N = 1000
A = [i for i in range(1,N+1)]
random.seed(0)

random.shuffle(A)
print(A)
MOD = 1000000007
fact = [1] * (N+1)
for n in range(1,N+1):
    fact[n] = fact[n-1] * n % MOD


A_b = bin(N)
ST = SegmentTree(N)
a=0
for i in range(N):
    a += (A[i]-1 - ST.query(0,A[i]+1)) * fact[N-i-1]
    a = a%MOD
    ST.update(A[i],1)
a+=1
a%=MOD
print(a)


