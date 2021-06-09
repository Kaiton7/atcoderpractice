N, M = map(int, input().split())
K = []
S = []
for _ in range(M):
    ks = list(map(int, input().split()))
    K.append(ks[0])
    S.append(ks[1:])
P = list(map(int,input().split()))
res = 0
for i in range(1<<N):
    Kswitch = [0 for i in range(M)]

    for j in range(N):
        #print(i)
        if 1&(i>>j)==1:
            for ix, s in enumerate(S):
                #print(s)
                if j+1 in s:
                    Kswitch[ix]+=1
    flag = True
    #print("kswitch",Kswitch)
    for ii in range(M):
        if Kswitch[ii]%2!=P[ii]:
            flag = False
    if flag:
        res+=1
    #print(i,res)
print(res)



