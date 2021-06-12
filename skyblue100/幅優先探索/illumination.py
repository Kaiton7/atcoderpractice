## 六角形なので、移動できる座標に注意する
## 垂直方向の偶奇数で変化する
## 周りに一周白を足して、外から到達できるところを調べる　
## 各白マスでクロマスに接している辺は他のマスでは絶対に
## デてこない変なので、各マスを走査するときに一緒に確認する。


def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
def LS():
    return list(input().split())

from collections import deque
import copy


W,H = LI()

field = [LI() for i in range(H)]

field.insert(0, [0]*(W+2))
for h in range(H):
    field[h+1].insert(0,0)
    field[h+1].append(0)
field.append([0]*(W+2))


dc = [1,-1,-1,-1, 0, 0]
dr = [0, 0,-1, 1, 1,-1]
res = 0
def solve(mr, mc):
    global res
    d = deque()
    d.append([mr,mc])
    field[mr][mc] = 2

    while d:
        r,c = d.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]

            if r%2==1 and i>1:
                nc+=1
            if nr<0 or nc<0 or nr>H+1 or nc > W+1:
                continue
            if field[nr][nc] == 0:
                field[nr][nc]=2
                d.append([nr,nc])
            if field[nr][nc]==1:
                res+=1

solve(0,0)
print(res)

            












