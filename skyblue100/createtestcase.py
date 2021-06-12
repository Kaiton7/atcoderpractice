N = 10**6
Q = 10**5
import random

with open("./autotest.txt", mode = "w") as f:
    t = str(N)+" "+str(Q) +"\n"
    f.write(t)
    for i in range(N-1):
        a = random.randint(1,N-1)
        b = random.randint(a+1,N)
        t = str(a)+" "+str(b) +"\n"
        f.write(t)
    for i in range(Q):
        p = random.randint(1,N)
        x = random.randint(1,10000)
        t = str(p)+" "+str(x) +"\n"
        f.write(t)