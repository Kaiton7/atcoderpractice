def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N = II()
R = []
C = []
for i in range(N):
    r,c = LI()
    R.append(r)
    C.append(c)


matrix = [R[0]]+[c for c in C]
#print(matrix)

DP = [[0]*(N+1) for i in range(N+1)]
for i in range(1,N+1):
    DP[i][i] = 0
#print(N)
for length in range(1,N):
    for i in range(1,N-length+1):
        j = i+length
#        print("length,i,j",length,i,j)
        DP[i][j] = 10**13
        for k in range(i,j):
#            print("i,j,k", i,j,k)
            #print(DP)
            t = matrix[i-1]*matrix[k]*matrix[j] + DP[i][k] + DP[k+1][j]
            #print(t)
            DP[i][j] = min(DP[i][j], t)
#print(DP)
print(DP[1][N])
