def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
def LS():
    return list(input().split())

R,C = LI()

field = [input() for i in range(R)]


def IsOk(r,c):
    if -1<r<R and -1<c<C:
        return True
    return False
dx,dy = (1,0,-1,0), (0,1,0,-1)

from collections import deque
stack = deque([[0,0]])
v = [[-1]*C for i in range(R)]
v[0][0] = 0
while stack:
    nr, nc = stack.popleft()
    #print(nr,nc)
    for ix in range(len(dx)):
        if IsOk(nr+dx[ix], nc+dy[ix]) and field[nr+dx[ix]][nc+dy[ix]]!="#" and v[nr+dx[ix]][nc+dy[ix]]==-1:
            v[nr+dx[ix]][nc+dy[ix]] = v[nr][nc] + 1
            stack.append([nr+dx[ix], nc+dy[ix]])
kuro = 0
for s in field:
    for ss in s:
        if ss=="#":
            kuro+=1

#print(v[R-1][C-1])
#print(kuro)
if v[R-1][C-1]==-1:
    print(-1)
else:
    print(R*C - kuro - (v[R-1][C-1]+1))




