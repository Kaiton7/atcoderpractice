from itertools import accumulate
from collections import deque
from heapq import heappush, heappop
from inspect import currentframe
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
def chkprint(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))


import sys
from heapq import *
import numpy as np
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def from_read(dtype=np.int64):
    return np.fromstring(read().decode(), dtype=dtype, sep=' ')
 
 
def from_readline(dtype=np.int64):
    return np.fromstring(readline().decode(), dtype=dtype, sep=' ')
 
def main(A, B, C, D):
    N = len(A)
    if N == 1:
        return True
    chkprint(A)
    A = A * N
    B = B * N
    C = C * N
    D = D * N
    # 重心を原点にする
    chkprint(A)
    A -= A.sum() // N
    B -= B.sum() // N
    C -= C.sum() // N
    D -= D.sum() // N
    chkprint(A)
    i = np.argmax(A * A + B * B)
    """print(A)
    print(B)
    print(C)
    print(D)"""
 
    EPS = 10**-8
 
    # i を j に重ねるとして判定
    for j in range(N):
        if C[j]**2 + D[j]**2 != A[i]**2 + B[i]**2:
            continue
 
        def check():
            se = set((C[k], D[k]) for k in range(N))
            a = complex(C[j], D[j]) / complex(A[i], B[i])
            for k in range(N):
                z = complex(A[k], B[k]) * a
                x = int(round(z.real))
                y = int(round(z.imag))
                if abs(z.real - x) > EPS:
                    return False
                if abs(z.imag - y) > EPS:
                    return False
                if (x, y) not in se:
                    return False
            return True
 
        if check():
            return True
    return False
 
N = int(readline())
pts = from_read().reshape(N + N, 2)
 
A, B = pts[:N].T
C, D = pts[N:].T
 
print('Yes' if main(A, B, C, D) else 'No')

"""
N = II()

S,T = [],[]
# 在るN_sとN_tに対して必要な変換を決めて、その変換を全てに行う
# それを全部のペア10*4に対して試す
import numpy as np
from numpy import linalg as LA
for _ in range(N):
    a,b = LI()
    S.append(np.array([a,b]))
tset  = set()
for _ in range(N):
    a,b = LI()
    T.append(np.array([a,b]))
    tset.add((a,b))
print(S)

def RAD(s,t):
    i = np.inner(s, t)
    n = LA.norm(s) * LA.norm(t)

    c = i / n
    a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))
    print("theta",a)  # 90.0
    return a
def rotation_o(u, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])

    return  np.dot(R, u)

for isx, s in enumerate(S):
    for itx, t in enumerate(T):
        if (s[0]==0 and s[1]==0) or (t[0]==0 and t[1]==0):
            x_s,y_s = t[0]-s[0], t[1]-s[1]
            allmatch = True
            for isxx, ss in enumerate(S):
                if isxx== isx:
                    continue
                #ss_r = rotation_o(ss, theta,True)
                ss_rxy = (round(ss[0]+x_s), round(ss[1]+y_s))
                chkprint(ss_rxy)
                if ss_rxy not in tset:
                    allmatch=False
                    break
            if allmatch:
                print("Yes")
                exit()
        else:
            theta = RAD(s,t)
            # sをtに移動させる
            # 回転
            s_r = rotation_o(s, theta, True)
            chkprint(s_r)
            # 平行移動
            x_s,y_s = t[0]-s_r[0], t[1]-s_r[1]

            allmatch = True
            for isxx, ss in enumerate(S):
                if isxx== isx:
                    continue
                ss_r = rotation_o(ss, theta,True)
                ss_rxy = (round(ss[0]+x_s), round(ss[1]+y_s))
                chkprint(ss_rxy)
                if ss_rxy not in tset:
                    allmatch=False
                    break
            if allmatch:
                print("Yes")
                exit()

print("No")


"""