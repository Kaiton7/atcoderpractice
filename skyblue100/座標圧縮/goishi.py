#偶数で色が異なっていたときに
# 一番最後だけじゃなくて、その次とも併合する必要が在る

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

from collections import deque
N = II()
g = II()
q = deque([{g:1}])

for i in range(2,N+1):
    g = II()
    b = q.pop()
    if i%2==0:
        if g in b:
            b[g]+=1
        else:
            if len(q)>0:
                b[g] = b[1-g]+1
                b2 = q.pop()
                b[g]+=b2[g]
                b.pop(1-g)
            else:
                b[g] = b[1-g]+1
                b.pop(1-g)
        q.append(b)
    else:
        
        if g in b:
            b[g]+=1
            q.append(b)
        else:
            c = {}
            c[g] = 1
            q.append(b)
            q.append(c)
ans = 0
#print(q)
while q:
    a = q.pop()
    ans+=a.get(0,0)

print(ans)
            

    
