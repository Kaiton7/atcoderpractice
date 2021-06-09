import itertools
N = int(input())
L = [tuple(map(int, input().split())) for i in range(N)]
ans_s = 0
ans_c = 0
for l in itertools.permutations(L):
    ans_c+=1
    f = True
    #print(l)
    for x, y in l:
        if f:
            x_,y_ = x,y
            f = False
        else:
            ans_s += ((x_-x)**2 + (y_-y)**2)**(1/2)
            #print("plus s")
            x_,y_ = x,y
    #print(ans_s)

#print(ans_s,ans_c)
print(ans_s/ans_c)

