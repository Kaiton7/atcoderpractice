# imos法の木バージョン
# 各頂点に足すべきスコアを最初に全て計算しておく
#  最後に根から順番に伝搬させていく
# 計算量? O(QE)がO(Q + E)？
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N,Q = LI()

Edge = [[] for _ in range(N)]

for i in range(N-1):
    a = LI()
    Edge[a[0]-1].append(a[1]-1)
    Edge[a[1]-1].append(a[0]-1)

C = [0 for _ in range(N)]
from collections import deque
PLUS=[list(map(int,input().split())) for i in range(Q)]

SCORE=[0]*(N+1)
for p,x in PLUS:
    SCORE[p-1]+=x
stack = deque([0])
used = [0]*(N+1)
used[0]=1
while stack:
    q = stack.pop()
    for to in Edge[q]:
        if used[to]==0:
            used[to] = 1
            SCORE[to] += SCORE[q]
            
            stack.append(to)

print(*SCORE[:-1])