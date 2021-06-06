from sys import stdin
input = stdin.readline
A,B,C,X,Y = map(int, input().split())  # 3個の数字の入力を受け取る

res = 10**10
for ab in range(2*max(X,Y)+1):
    cc = 2*C*ab

    x = X-ab
    y = Y-ab

    if x>0:
        cc+= A*x
    if y>0:
        cc+= B*y
    res = min(cc,res)
print(res)
