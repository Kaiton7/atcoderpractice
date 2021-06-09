R,C = map(int, input().split())
X = [list(map(int,input().split())) for i in range(R)]
revX = []
for i in range(len(X)):
    a = []
    for x in X[i]:
        if x==1:
            a.append(0)
        else:
            a.append(1)
    revX.append(a)
ans = 0
for i in range(1<<R):
    gl = []
    res = 0
    for j in range(R):
        if 1&(i>>j)==1:
            gl.append(revX[j])
        else:
            gl.append(X[j])
        
    for c in range(C):
        sen = 0
        for gg in gl:
            sen+=gg[c]
        if sen>R//2:
            res+=sen
        else:
            res+=R-sen
    ans = max(res,ans)
print(ans)