def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

M = II()
N = II()
field = [[0]*(M+2) for i in range(N+2)]
for i in range(1, N+1):
    field[i][1:M+1] = LI()


dx = (1,0,-1,0)
dy = (0,1,0,-1)
def dfs(r,c,vis):
    #番外、氷じゃなかったら返ってくる
    res = 0
    vis[r][c] = 0
    for i in range(len(dx)):
        if vis[r+dx[i]][c+dy[i]]:
            res = max(dfs(r+dx[i],c+dy[i],vis),res)
    vis[r][c] = 1
    return res+1

ans = 0
for r in range(N):
    for c in range(M):
        #rint(r,c)
        if field[r][c]:
            ans = max(ans,dfs(r,c,field))
print(ans)