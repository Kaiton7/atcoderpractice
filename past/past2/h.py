N,M = map(int,input().split())
from collections import defaultdict
d=defaultdict(list)
a1,a2,a3,a4,a5,a6,a7,a8,a9 = [],[],[],[],[],[],[],[],[]
for n in range(N):
	dd = input()
	for m,val in enumerate(dd):
		if val=="S" or val=="G":
			d[val].append([n,m])
		else:
			d[int(val)].append([n,m])

if len(d)<11:
	print(-1)
	exit()

pre = 100000
res = []
tmp = 0
for i in d[3]:
	for j in d[2]:
		for k in d[1]:
			tmp = abs(d["S"][0][0]-k[0]) + abs(d["S"][0][1]-k[1])
			tmp  += abs(k[0]-j[0]) + abs(k[1] - j[1])
			tmp  += abs(i[0]-j[0]) + abs(i[1] - j[1])
			if tmp<pre:
				pre  = tmp
	res.append([i[0],i[1],tmp])
tmp = 0
pre = 100000
res2 = []
for i in d[6]:
	for j in d[5]:	
		for k in res:
			#tmp = abs(d["S"][0][0-k[0]) + abs(d["S"][0][1]-k[1])
			tmp  += k[2]+abs(k[0]-j[0]) + abs(k[1] - j[1])
			tmp  += abs(i[0]-j[0]) + abs(i[1] - j[1])
			if tmp<pre:
				pre  = tmp
	res2.append([i[0],i[1],tmp])


tmp = 0
pre = 100000
res = []
for i in d[8]:
	for j in d[9]:	
		for k in res2:
			#tmp = abs(d["S"][0][0-k[0]) + abs(d["S"][0][1]-k[1])
			tmp  += k[2]+abs(k[0]-j[0]) + abs(k[1] - j[1])
			tmp  += abs(i[0]-j[0]) + abs(i[1] - j[1])
			if tmp<pre:
				pre  = tmp
	res.append([i[0],i[1],tmp])
ans = []
for i in res:
	ans.append(i[2]+abs(i[0]-d["G"][0][0]) + abs(i[1] - d["G"][0][1]))
print(min(ans))
