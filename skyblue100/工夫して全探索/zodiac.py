M  = int(input())
Z = [tuple(map(int, input().split())) for i in range(M)]
N = int(input())
Y = [tuple(map(int, input().split())) for i in range(N)]


Ys = set(Y)
for z in Z:
    for y in Y:
        vx = z[0]-y[0]
        vy = z[1]-y[1]
        f=True
        for zz in Z:
            
            if (zz[0] - vx, zz[1]-vy) not in Ys:
                f =False
                break
        if f:
            print(-vx,-vy)
            exit()