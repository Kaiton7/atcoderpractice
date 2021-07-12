def LI():
    return list(map(int, input().split()))
def II():
    return int(input())
N = II()

print(int(N*(N-1)//2))
for i in range(999999899,1000000000):
    if int(i*(i-1)/2) != int(i*(i-1)//2):
        print("missig",i)
        print(int(i*(i-1)/2), int(i*(i-1)//2))
print("finish")


"""
NN = [i for i in range(1,N+1)]
NN = NN+NN
ans = 0
import itertools
#print(len(list(itertools.permutations(NN,N))))

t = 0
i = 1
for ix,x in enumerate(NN[i:N+i]):
    t +=(ix+1)%x
ans = max(t,ans)
print(ans)
"""