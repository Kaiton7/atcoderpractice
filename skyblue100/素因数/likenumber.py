def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
sosuu = set()
sosuu.add(2)
A = 100000+1
for L in range(3, A, 2): # 2 以外の素数は奇数なので
    for L2 in sosuu:
        if L % L2 == 0:
            break # 素数でないことがわかったらそれ以上ループする必要はない
    else: # break で抜けることがなかったら L は素数（Python 特有の制御構文）
        sosuu.add(L)
#累積和
B = [0]*(A)
for L in range(3,A,2):
    #print(L,(L+1)//2, (L+1)//2 in sosuu)
    if L in sosuu and (L+1)//2 in sosuu:
        B[L] = B[L-2]+1
        B[L-1] = B[L-2]
    else:
        B[L-1] = B[L-2]
        B[L] = B[L-1]
#print(B)
Q = II()

for i in range(Q):
    l,r = LI()
    #print(r, l, B[r], B[l-1])
    print(B[r]-B[l-1])

        