N = int(input())

Dig= []

for i in range(N):
    Dig.append(list(map(int, input().split()))[2:])

C,In,Out = [0]*N,[0]*N,[0]*N
t = 0
def dfs(e):
    global t
    if C[e]==1:
        return 
    t+=1    
    C[e] = 1
    In[e] = t
    
    for g in Dig[e]:
        if C[g-1]==1:
            continue
        dfs(g-1)
        #t = t+1
    t+=1
    Out[e] = t

for i in range(N):
    dfs(i)

for i in range(N):
    print(i+1,In[i],Out[i])

