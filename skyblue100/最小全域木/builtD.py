
# 座標の各次元ごとに辺を持つと考える。
# 全ての辺をリストアップしてクラスかる法
# 辺の数が二倍になるからループの数も注意して
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = 10**10

from collections import deque
from heapq import heappush, heappop

class UnionFind():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rnk = [0]*(n+1)

    # ノードxのrootノードを見つける
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def Unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        # すでに同じ木に属していた場合
        if(x == y):
            return 
        # 違う木に属していた場合rnkを見てくっつける方を決める
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rnkが同じ（深さに差がない場合）は1増やす
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    # ノードxが属する木のサイズを返す
    def Count(self, x):
        return -self.root[self.Find_Root(x)]
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = 10**10

def solve(N):
    X = []
    Y = []
    for i in range(N):
        x, y = LI()
        X.append((x, i))
        Y.append((y, i))
    X.sort(), Y.sort()
    Alld = []
    for i in range(N-1):
        #print(X[i+1],X[i],Y[i+1],Yffdfdfdddddddf[i])
        Alld.append((X[i+1][0]-X[i][0], X[i+1][1], X[i][1]))
        Alld.append((Y[i+1][0]-Y[i][0], Y[i+1][1], Y[i][1]))
    #Alld = Xd+Yd
    Alld.sort()
    #print(Alld)
    #Xd.sort(), Yd.sort()
    #print("D",D)
    U = UnionFind(N)
    ans = 0
    for i in range(len(Alld)):
        d,i,j = Alld[i]
        if U.isSameGroup(i,j):
            continue
        U.Unite(i,j)
        ans += d
        if U.Count(i)==N:
            break
    print(ans)

N = II()
solve(N)