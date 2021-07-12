# todo:約数列挙のenumsqrtを実装

from sys import stdin
input = stdin.readline

N = int(input())

re = 0
def enumdiv(n):
    S = []
    i = 1
    while i*i<=n:
        if n%i==0:
            S.append(i)
            if i*i!=n:
                S.append(n//i)
        i+=1
    return S
for i in range(1,N+1,2):
    v = enumdiv(i)
    if len(v)==8:
        re+=1
print(re)
