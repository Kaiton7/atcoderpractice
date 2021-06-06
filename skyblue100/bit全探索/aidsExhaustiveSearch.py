N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

flag = [False]*2000
for i in range(1<<len(A)):
    n = 0
    for j in range(len(A)):
        if (i >> j)&1==1:
            n += A[j]
    flag[n] = True
for m in M:
    print("yes" if flag[m] else "no")

"""
for m in M:
    f = False
    for i in range(2**N):
        j = 0
        res = 0
        #print("iteration", i)
        while i>0:
            #print("i, i&1",i,i&1)
            if i&1:
                res+=A[j]
            j+=1
            #print("res:",res)
            if res==m:
                i=2**N-1
                #print("fit!!")
                f = True
                break
            if res > m:                
                break
            #print(i,j)
            i= i>>1
            #print("after shift i ",i)
        if f:
            break
    #print("res initiated ", res,i)
    if f:
        print("yes")
    else:
        print("no")
        
"""