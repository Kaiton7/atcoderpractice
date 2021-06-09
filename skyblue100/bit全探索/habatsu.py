N, M = map(int, input().split())
P = [tuple(map(int,input().split())) for i in range(M)]
res = 1
Ps = set(P)
for i in range(1<<N):
    gl = []
    for j in range(N):
        if 1&(i>>j)==1:
            gl.append(j+1)

    f = True
    for gi in range(len(gl)):
        for ki in range(gi+1, len(gl)):
            if (gl[gi],gl[ki]) not in Ps:
                f = False
    if f:
        res = max(res, len(gl))
print(res)