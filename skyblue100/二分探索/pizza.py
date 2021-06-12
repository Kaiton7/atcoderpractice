def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

D = II()
N = II()
M = II()

Shop = [II() if i!=0 else i for i in range(N)]
Shop = Shop + [D]
Orders = [II() for i in range(M)]
Shop.sort()

#print(Shop)
def IsOkB(index:int, key:int, A:list):
	if A[index] >= key:
		return True
	else:
		return False
def IsOkA(index:int, key:int, A:list):
	if A[index] <= key:
		return True
	else:
		return False
def MeguruBsearch(key:int,A:list,f):
	ng = -1
	ok = len(A)
	while (abs(ok-ng)>1):
		mid=(ok+ng)//2
		if f(mid,key,A):
			ok = mid
		else:
			ng = mid
	return ok

total = 0
for order in Orders:
    #kA = MeguruBsearch(order, Shop,IsOkA)
    kB = MeguruBsearch(order, Shop, IsOkB)
    #print(order,kB-1,kB)
    #print("(order,orderより小さい最大,orderより大きい最小)",order,kB-1,Shop[kB-1],kB,Shop[kB])
    total += min(abs(Shop[kB-1]-order),abs(Shop[kB]-order))
print(total)
