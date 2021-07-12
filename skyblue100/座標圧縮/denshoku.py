def LI():
    return list(map(int, input().split()))
def II():
    return int(input())


N = LI()

C = LI()
a = C.pop()
d=1
res = []

while C:
    if a==C[-1]:
        res.append(d)
        a = C.pop()
        d = 1
    else:
        d+=1
        a = C.pop()
res.append(d)

#for i in range(len(res)-2):
#    a=  max(a,sum(res[i:i+3]))
#print(a)
if len(res)<3:
    print(sum(res))
else:
    print(max(sum(res[i:i+3]) for i in range(len(res)-3)))