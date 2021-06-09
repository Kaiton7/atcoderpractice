class SegmentTree:
	def __init__(self,n:int,data:list) -> None:
		N = 1
		while (N < n):
			N*=2
		self.NodeSize = N
		self.Array = [0]*(2*self.NodeSize-1)
		for i in range(n):
			self.Array[i+n-1] = data[i]
		for i in range(n-2,-1,-1):
			self.Array[i] = max(self.Array[2*i+1],self.Array[2*i+2])
		
	def update(self, ix:int, val:int):
		ix += self.NodeSize - 1
		self.Array[ix] = val
		while ix >0:
			ix = (ix-1)//2
			self.Array[ix] = max(self.Array[2*ix+1],self.Array[2*ix+2])

	def getmax(self, a:int, b:int, k:int=0, l:int=0, r:int=-1):
		if r<0:
			r = self.NodeSize
		if r <= a or b <= l:
			return -1000000
		if a <= l and r <= b:
			return self.Array[k]
		
		vl = self.getmax(a, b, 2*k+1, l, (l+r)//2)
		vr = self.getmax(a, b, 2*k+2, (l+r)//2, r)
		return max(vl, vr)

def IsOk(arg,):
	pass

def MeguruBisect(ng, ok):
	'''
	初期値のng, okを受け取りIsOkを満たす最小(最大)のokを返す
	'''
	while (abs(ok-ng)>1):
		mid=(ok+ng)//2
		if IsOk(mid):
			ok = mid
		else:
			ng = mid
	return ok
def IsOkB(index:int, key:int, A:list):
	if A[index] >= key:
		return True
	else:
		return False
def MeguruBsearch(key:int,A:list):
	ng = -1
	ok = len(A)
	while (abs(ok-ng)>1):
		mid=(ok+ng)//2
		if IsOkB(mid,key,A):
			ok = mid
		else:
			ng = mid
	return ok

def LIS(A:list):
	seg = SegmentTree(len(A), [0]*len(A))
	aval = A.copy()

	aval.sort()
	res = 0
	for i in range(len(A)):
		h = MeguruBsearch(A[i], aval)
		h+=1

		val = seg.getmax(0, h)

		if seg.getmax(h,h+1) < val+1:
			seg.update(h, val+1)
			res=  max(res, val+1)
	
	return res

N = int(input())
A = list(map(int,input().split()))

print(LIS(A))
