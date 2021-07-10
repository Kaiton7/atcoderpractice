
def LI():
    return list(map(int, input().split()))
def II():
    return int(input())


N = II()
D = []
for i in range(N):
    t,l,r = LI()
    if t==1:
        D.append([l,r])
    elif t==2:
        D.append([l,r-0.1])
    elif t==3:
        D.append([l+0.1,r])
    else:
        D.append([l+0.1,r-0.1])
cnt=0
for i in range(len(D)):
    for j in range(i+1,len(D)):
        if D[i][0]<D[j][0]:
            if D[i][1]>=D[j][0]:
                cnt+=1
        else:
            if D[j][1]>=D[i][0]:
                cnt+=1
#print(D)
print(cnt)


