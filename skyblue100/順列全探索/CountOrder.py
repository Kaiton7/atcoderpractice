import itertools
N =  int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))


# BITで区間和を持つ
# LSBを考えるのがポイント
# 区間に足す時はLSBを足していくと、木を上がっていける
# 区間和をかんがえる時はLSBを引いていくと、そこまでの区間を全部足せる
# LSBはk&(-k)でできる
# ニの補数表現になるので、最後の1が残る
# 肝心の数え上げは左側から各桁ごとにその桁の観点でそれより小さいものを見ていけば良い
# 一桁目がxなら少なくとも(x-1)*(N-1)!個は小さいものが在る
# 一桁目がxの場合もその右隣の者を確認して、右隣の数-1以下のものを選べばよいが、既に使っている数は使えないことに気をつける。
# 45132のとき一桁目が4の場合、二桁目が5未満の必要がある。
# その場合の二桁目は1,2,3,4が考えられるが、4は既に使っているので抜く
# じゃあどうやってその桁までに使った数を記憶しておくのか
# BITを使う、add(i,x)でi桁目がxだったときに、xを1にする
# get(i)でi桁目までに使われている数を調べる。
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

