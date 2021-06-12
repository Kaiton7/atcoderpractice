def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

while True:
    F = LI()
    if F[0]==0 and F[1]==0:
        break
    M = [LI() for _ in range(F[1])]
    C = [[0 for _ in range(F[0])] for j in range(F[1])]
    res = 0
    for i in range(F[1]):
        for j in range(F[0]):
            if C[i][j]!=1 and M[i][j]==1:
                res +=1
                stack = [(i,j)]
                while stack:
                    r, c = stack.pop()
                    if C[r][c] == 1:
                        continue
                    C[r][c] = 1
                    for dx,dy in [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1)]:
                        if r+dx>-1 and c+dy>-1 and r+dx <F[1] and c+dy<F[0] and M[r+dx][c+dy]==1:
                            stack.append((r+dx,c+dy))

    print(res)    
            
            

        