def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
def LS():
    return list(input().split())

R,C = LI()
sr, sc = LI()
sr,sc = sr-1,sc-1
gr, gc = LI()
gr,gc = gr-1,gc-1

field = [input() for i in range(R)]



dx,dy = (1,0,-1,0), (0,1,0,-1)

from collections import deque
stack = deque([[sr,sc]])
v = [[-1]*C for i in range(R)]
v[sr][sc] = 0
while stack:
    nr, nc = stack.popleft()
    #print(nr,nc)
    for ix in range(len(dx)):
        if field[nr+dx[ix]][nc+dy[ix]]!="#" and v[nr+dx[ix]][nc+dy[ix]]==-1:
            v[nr+dx[ix]][nc+dy[ix]] = v[nr][nc] + 1
            stack.append([nr+dx[ix], nc+dy[ix]])

print(v[gr][gc])




