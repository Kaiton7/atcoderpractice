
## 1文字
# abc
N = int(input())
s= []
for i in range(N):
    a = list(map(int, input().split()))
    #print(a[0])
    s.append((a[0],a[1]))

hashiraset = set(s)
ans = 0
for i in range(N):
    x0 = s[i][0]
    y0 = s[i][1]
    for j in range(i,N):
        x1 = s[j][0]
        y1 = s[j][1]
        vx = x1 - x0
        vy = y1 - y0
        if (x0+vy, y0-vx) in hashiraset and (x1+vy,y1-vx) in hashiraset:
            ans = max(ans, vx**2 + vy**2)
        elif (x0-vy, y0+vx) in hashiraset and (x1-vy,y1+vx) in hashiraset:
            ans = max(ans, vx**2 + vy**2)
print(ans)