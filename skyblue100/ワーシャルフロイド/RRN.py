# 全部の辺が在る状態から初めて
# 全経路について、回り道をした場合の最短距離を求める
# もし直接行くよりも近ければそのグラフは存在しない
# もし直接行くよりも遠ければ直接行く辺はの個数必要が在る
# もし同じなら削除しても良い
# 削除しても、回り道する経路を使えばよいの他の頂点間の
# 最短距離にも影響しない

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
INF = 10**10

N = II()
A = [LI() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j]==0:
            A[i][j]= INF 


for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j]==INF:
                continue
            t = A[i][k] + A[k][j]
            if A[i][j] > t:
                print(-1)
                exit()
            if A[i][j]==t:
                # 辺を消す
                A[i][j]=INF
res = 0
for i in range(N):
    for j in range(i+1,N):
        if A[i][j]==INF:
            continue
        res += A[i][j]

            
print(res)