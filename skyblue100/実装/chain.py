from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe


def LI():
    return list(map(int, input().split()))

def II():
    return int(input())

def chkprint(*args):
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg), '???')+' = '+repr(arg) for arg in args))


while True:
    H = II()
    if H==0:
        break
    field = [LI() for _ in range(H)]
    fieldpan=[[0]*5 for _ in range(H)]
    field = fieldpan+field
    #chkprint(field)
    Smap=[[0]*5 for _ in range(H)]
    Smap=fieldpan+Smap
    ans=0
    print("++++++++++++++++++++")
    while True:
        flag = True
        print("====================")
        for h in range(H,2*H):
            prev=-1
            cnt=0
            tp = 0
            ixlist=[]
            for ix, he in enumerate(field[h]):
                ixx=Smap[h][ix]
                he=field[h-ixx][ix]
                if he==prev:
                    cnt+=1
                    tp+=he
                    ixlist.append(ix)
                else:
                    if cnt>=3:
                        break
                    cnt=1
                    tp = he
                    ixlist=[]
                prev=he
            # 上の分も全て足して増やしていく
            if cnt>=3:
                ans+=tp
                flag=False
                for fh in range(H,h+1):
                    for ix in ixlist:
                        Smap[fh][ix]+=1
            #print(h,tp)
            for sss in Smap:
                print(sss)
            #print(field)

        if flag:
            break
    #print("hjeeeeeeee")
    #chkprint(ans)
    print(ans)