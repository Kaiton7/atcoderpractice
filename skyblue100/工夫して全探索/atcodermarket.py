N = int(input())

A,B= [],[]
midd =0
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
    midd += abs(a-b)

A.sort()
B.sort()

s = A[N//2]
t = B[N//2]
ans = 0
for a, b in zip(A, B):
    ans += abs(a-s)
    ans += abs(b-t)
ans+=midd

print(ans)
