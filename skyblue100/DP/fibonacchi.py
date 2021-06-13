N = int(input())


dp = [1]*(N+1)

if N==0 or N==1:
    print(1)

else:
    for n in range(2,N+1):
        dp[n] = dp[n-1]+dp[n-2]
    print(dp[N])
