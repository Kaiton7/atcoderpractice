def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()

varn = 0

for i in range(1000):
    if N==(i*(i-1))/2:
        varn  = i
        break


if varn==0:
    print("No")

V = [[] for n in range(varn)]

k = 1

for i in range(varn):
    for j in range(i+1,varn):
        V[i].append(k)
        V[j].append(k)
        k+=1
if varn!=0:
    print("Yes")
    print(varn)
    for i in range(varn):
        print(varn-1, " ".join(map(str, V[i])))
    


        
