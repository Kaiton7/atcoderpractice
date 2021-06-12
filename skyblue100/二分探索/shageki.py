
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())


N = II()
F = [LI()+[] for i in range(N)]



def XisOk(A, mid):
    stone = [0]*N
    for a in A:
        v = (mid-a[0])//a[1]
        if v<N:
            stone[v]+=1
    count = 0
    for i in range(N):
        count+=stone[i]
        if i+1 <count:
            return False
    return True

def BS(A):
    ng = max([_[0] for _ in A])-1
    #ng = -1
    ok = 10**16
    while abs(ng-ok)>1:
        mid = (ok+ng)//2
        if XisOk(A,mid):
            ok = mid
        else:
            ng = mid
    return ok

print(BS(F))










