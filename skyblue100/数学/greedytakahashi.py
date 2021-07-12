def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

A,B,K = LI()

if A < K:
    B = B - (K-A)
    if B<0:
        print(0,0)
    else:
        print(0,B)
else:
    print(A-K,B)
