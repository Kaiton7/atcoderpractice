Q = int(input())
from collections import deque
D = deque()
K = {}
for _ in range(Q):
	t,*a  = input().split()
	if t=="1":
		D.append(a)
	else:
		n = int(a[0])
		while len(D)>0 and int(D[0][1])<=n:
			d = D.popleft()
			n-=int(d[1])
			if d[0] in K:
				K[d[0]] = K[d[0]]+int(d[1])
			else:
				K[d[0]] = int(d[1])
			
		if len(D)>0 and n>0:
			if D[0][0] in K:
				K[D[0][0]] = K[D[0][0]]+n
			else:
				K[D[0][0]] = n
			D[0][1] = int(D[0][1]) -n
		res = 0
		for v in K.values():
			res +=v**2
		print(res)
		K={}