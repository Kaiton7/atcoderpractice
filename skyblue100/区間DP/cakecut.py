def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
import numpy as np 
N = int(readline())
#print(N)
A = np.array(read().split(),np.int64)
A = np.concatenate([A, A])
dp = np.zeros(N, np.int64)
#print(A,dp)
for n in range(1,N+1):
    dp = np.append(dp, dp[0])
    print(dp)
    # 今までに取り進めた数を確認するN
    # IOIから始めるので偶奇でIOIJOIどっちが取るか決まる
    player= (N-n)&1
    if player ==0:
        # n個になるときにケーキを取ったのがIOIなので次はJOIが選べる
        # 左側を取ったときのleftと右側を取ったときのrightの大きい方を取る
        # dp[i]:i番目からi+n番目までのケーキが残っているときの最大値
        # dp[1:N+1]1つずらす？dp[1:N+1]+A[:N]1つずらしたものとずらす前のものを足す
        # ので、左側を取ることになる？
        # dp[:N]そのまま、dp[:N]+A[n-1:N+n-1]nの分だけAを左にずらすので、dpから見るとn分だけ
        # 右に進んだ切れ端を取ることになる。
        # 
        left = dp[1:N+1] + A[:N]
        right = dp[:N] + A[n-1:N+n-1]
        print(A)
        print(left,right,A[n-1:N+n-1])
        dp = np.maximum(left, right)
        print("after max",dp)
    else:
        # n個になるときにケーキを取ったのがJOI次はIOIが選ぶが取れるものの中で最大
        # のものを取る
        # IOIは切れ端の大きさだけ見て決めるので
        # 今獲得できる切れ端を比較するA[:N]とA[n-1:N+n-1]がそれ
        # A[:N]の方が大きい時は、そちらを取られるのでdp[1:N+1]がJOIの得点となる
        # 
        print("here",n)
        print("A[:N]",A[:N]," > A[n-1:N+n-1]",A[n-1:N+n-1])
        dp = np.where(A[:N] > A[n-1:N+n-1], dp[1:N+1], dp[:N])
        print("after where",dp)
#全ての地点からn個分離れた区間(1週)のなかでmaxを取る
answer = dp.max()
print(answer)


