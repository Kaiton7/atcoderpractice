# numpyのcumsumを使う
# 半開区間ということを忘れずに二次元累積和を使う

def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()
C = [0 for i in range(1000002)]
for _ in range(N):
    a,b = LI()
    C[a] += 1
    C[b+1] -= 1
res,res_p = 0,0
ans = 0
#print(C[:15])
for ic in range(len(C)):
    res+=C[ic]
    if res>res_p:
        ans = ic
        res_p = res
print(res_p)

