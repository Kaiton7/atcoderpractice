# 各チーズ屋を覚えておき、二点間のdfsをする

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
def LS():
    return list(input().split())


R,C,N = LI()
field = [input() for i in range(R)]
cheese = [0] *(N+1)
for ix, s in enumerate(field):
    
    for ixx, ss in enumerate(s):
        if ss=="S":
            cheese[0] = [ix, ixx]
        for n in range(1,N+1):
            if ss==str(n):
                cheese[n] = [ix, ixx]

dx,dy = (1,0,-1,0), (0,1,0,-1)
from collections import deque
allcost = 0
def IsIn(r,c):
    if r>-1 and r<R and c>-1 and c<C:
        return True
    return False
for ix, S in enumerate(cheese[:-1]):
    D = cheese[ix+1]
    stack = deque([[S[0],S[1]]])
    v = [[-1]*C for i in range(R)]
    v[S[0]][S[1]] = 0
    while stack:
        nr, nc = stack.popleft()
        if field[nr][nc] == ix+1:
            break
        #print(nr,nc)
        for ix in range(len(dx)):
            if IsIn(nr+dx[ix],nc+dy[ix]) and field[nr+dx[ix]][nc+dy[ix]]!="X" and v[nr+dx[ix]][nc+dy[ix]]==-1:
                v[nr+dx[ix]][nc+dy[ix]] = v[nr][nc] + 1
                stack.append([nr+dx[ix], nc+dy[ix]])
    allcost+= v[D[0]][D[1]]

print(allcost)