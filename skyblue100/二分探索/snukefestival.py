
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())


N = II()
A = LI()
B = LI()
C = LI()

A.sort()
#B.sort()
C.sort()

def IsOkB(index:int, key:int, A:list):
	if A[index] > key:
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

def IsOkA(index:int, key:int, A:list):
	if A[index] < key:
		return True
	else:
		return False
def MeguruBsearchA(key:int,A:list,f):
	ng = len(A)
	ok = -1
	while (abs(ok-ng)>1):
		mid=(ok+ng)//2
		if f(mid,key,A):
			ok = mid
		else:
			ng = mid
	return ok
res = 0

for b in B:
    ixa = MeguruBsearchA(b, A, IsOkA)
    ixc = MeguruBsearch(b, C, IsOkB)
    res += (ixa+1) * (len(C) - ixc)

print(res)