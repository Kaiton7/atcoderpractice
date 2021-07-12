
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

def distance(P1, P2):
    t = 0
    for i in range(3):
        t += (P1[i] - P2[i])**2
    t = t ** (1/2)
    t = max(0, t - (P1[3]+P2[3]))
    return t

def solve(N):
    Q = []
    D = []
    for _  in range(N):
        x,y,z,r = list(map(float, input().split()))
        Q.append([x, y, z, r])
    dist = [[INF for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            if i==j:
                continue
            t = distance(Q[i],Q[j])
            dist[i][j] = t
            dist[j][i] = t
            heappush(D, [t, i, j])
    #print("D",D)
    U = UnionFind(N)
    ans = 0
    while D:
        t,i,j = heappop(D)
        if U.isSameGroup(i,j):
            continue
        U.Unite(i,j)
        ans += t
        if U.Count(i)==N:
            break
    print("{:.3f}".format(ans))

def main():
    while True:
        N = II()
        if N==0:
            break
        solve(N)

main()
