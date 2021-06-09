N, K =  map(int,input().split())
A = list(map(int,input().split()))

res= 10**12

for i in range(2**N):
    BL = []
    #print(str(bin(i)))
    if str(bin(i)).count("1")!=K:
        continue
    # print(i)
    h, ans = 0,0

    for j in range(N):
        if (i>>j)&1==0:
            h = max(A[j],h)
            continue
        if h<A[j]:
            h = A[j]
            continue
        if h>=A[j]:
            ans += h-A[j]+1
            h+=1
            continue
    # print("i:",i,"bin(i):",bin(i),", calcprice:",calcprice(BL))
    res = min(res, ans)
    # print("")
print(res)

            






