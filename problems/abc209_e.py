from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
def chkprint(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))
N = II()

def num(c):
    if "a" <= c and c<= "z":
        return ord(c)-ord("a")
    else:
        return ord(c)-ord("A") + 26

def idx(S, flag):
    now = 0
    if flag:
        now = len(S)-3
    prex = 0
    for i in range(now, now+3):
        prex = prex*52 + num(S[i])
    return prex
SL =[]
M = 52**3
Edge = [[] for _ in range(M)]
cnt = [0]*M
for _ in range(N):
    s = input()
    SL.append(s)
    #逆に見ていく
    Edge[idx(s,True)].append(idx(s,False))
    # 有効辺が出ているかどうかで、勝ち負けを判断する最初のノードを決定する
    cnt[idx(s,False)]+=1
Q = deque()
dp= [2]*M
#有効辺が出ていない所から始める
for i in range(M):
    if cnt[i]==0:
        Q.append(i)
#print(N)
#print(Edge)

while Q:
    now =  Q.popleft()
    for nn in Edge[now]:
        if cnt[nn]==0:
            continue
        # 全ての有効辺の先から返ってきたか確認
        cnt[nn]-=1
        dp[nn] = min(2-dp[now], dp[nn])
        # 全ての有効辺を確認したか、または、そのノードがwinになっていれば次に勧める
        if cnt[nn]==0 or dp[nn]==0:
            cnt[nn] = 0
            Q.append(nn)

#ループ構造になっているもの、木になっているものの全てのcntが1以上の場合ループになっている
for i in range(M):
    if cnt[i]:
        dp[i] = min(dp[i], 1)

X = ["Aoki","Draw","Takahashi"]

for i in range(N):
    print(X[dp[idx(SL[i],True)]])

    
    


        


















#最初3文字と終わり三文字が一緒のものがあればDRAW
