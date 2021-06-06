

while True:
    n,x = map(int, input().split())  # 3個の数字の入力を受け取る
    if n==0 and x==0:
        break
    else:
        res = 0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                for k in range(j+1,n+1):
                    #print(i,j,k)
                    if i+j+k==x:
                        #print("in", i,j,k)
                        res+=1
                        j, k = n-1, n-1
        print(res)