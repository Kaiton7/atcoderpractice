n = int(input())
pos = [list(map(int, input().split())) for i in range(n)]

import sys
def comb(f1, f2):
    """2 つの 関数 を   合成 した 関数 を   返す """
    return lambda x:f1(f2(x))
# 対称 操作
REV  = lambda ls: list(reversed(ls))                            # 左右反転
USD  = lambda ls: [ len(ls)-x-1 for x in ls ]                   # 上下 反転
T90  = lambda ls: [ ls.index(x) for x in range(len(ls)) ]       # 90 度 回転
T180 = comb(USD, REV)                                           # 180 度 回転
T270 = comb(T90, T180)                                          # 270 度 回転
D1   = comb(REV, T90)                                           # 対角線 での 反転 その 1
D2   = comb(USD, T90)                                           # 対角線 での 反転 その 2




def is_dif(cols, sols):
    """ 対称性 を  考慮し ても 固有 の 解か """
    return all( tuple(op(cols)) not in sols for op in (REV, USD, T90, T180, T270, D1, D2) )
def queenok(col,new):
    for ix,c in enumerate(col):
        if abs(c-new)==abs(len(col)-ix):
            return False
    return True

def nqueen(k):
    solution = set()
    def qiter(col,rows):
        if rows:
            for r in rows:
                if queenok(col,r):
                    qiter(col+(r,), rows-{r})
                else:
                    pass
        if len(rows)==0:
            solution.add(col)
        return 0
    qiter(tuple(), frozenset(range(k)))
    return solution



def printmap(sol):
    field = [["." for i in range(8)] for j in range(8)]
    for ix, x in enumerate(sol):
        field[x][ix] = "Q"
    for f in field:
        print("".join(f))

if __name__=='__main__':
    sols=nqueen(8)
    #print ('N of solutions:', len(sols))
    for sol in sols:
        #print(sol)
        flag = True
        for p in pos:
            if sol[p[1]]!=p[0]:
                flag=False
                break
        if flag:
            printmap(sol)