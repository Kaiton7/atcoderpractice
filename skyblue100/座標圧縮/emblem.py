def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N,M = LI()
# M+N個の全てのペアについて取れる半径を考える

NP,MP = [],[]
for i in range(N):
    x,y,r = LI()
    NP.append([x,y,r])
for i in range(M):
    x,y = LI()
    MP.append([x,y])

for i in range(N+M):
    for j in range(i+1, N+M):
        

