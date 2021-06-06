from sys import stdin
input = stdin.readline

N = int(input())

re = 0
for i in range(1,N+1,2):
    v = set()
    for j in range(1,i+1,2):
        #print(i,j)
        if i%j==0:
            v.add(j)
            #print("vv",v)
    if len(v)==8:
        re+=1
print(re)
