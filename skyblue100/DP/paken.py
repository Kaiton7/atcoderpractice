def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()

field = ['' for i in range(N)]

for i in range(5):
    s = input()
    for ix,ss in enumerate(s):
        field[ix]+=ss
color = ("W","B","R")
dic = [{"W":10,"B":10,"R":10} for i in range(N)]
for ix, f in enumerate(field):
    for c in color:
        dic[ix][c] = 5-f.count(c)
p = {0:"W",1:"B",2:"R"}
DP = [[10**9]*3 for i in range(N)]
for i in range(3):
    DP[0][i] = dic[0][p[i]]
for ix, f in enumerate(field[1:]):
    for  a in range(3):
        for b in range(3):
            if a!=b:
                DP[ix+1][b] = min(DP[ix+1][b], DP[ix][a]+dic[ix+1][p[b]])
print(min(DP[N-1]))









