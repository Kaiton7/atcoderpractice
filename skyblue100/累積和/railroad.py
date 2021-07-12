# numpyのcumsumを使う
# 半開区間ということを忘れずに二次元累積和を使う

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N,M = LI()
C = [0 for i in range(1000002)]
P = LI()
for i in range(len(P)-1):
    if P[i]<P[i+1]:
        C[P[i]]+=1
        C[P[i+1]]-=1
    else:
        C[P[i]]-=1
        C[P[i+1]]+=1
ans = 0
for i in range(1,N):
    C[i] += C[i-1]
    a,b,c = LI()
    ans+= min(a*C[i], b*C[i]+c)
print(ans)

