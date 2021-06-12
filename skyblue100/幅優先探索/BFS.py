def LI():
    return list(map(int, input().split()))
def II():
    return int(input())

N = II()
Edge = [[] for i in range(N)]

for i in range(N):
    t=LI()
    Edge[i] = t[2:]

from collections import deque
stack = deque([1])
stack1 = deque()
COST = [10000000]*N
c = 0
visited = [0]*N
while stack:
    #print(stack)
    while stack:
        stack1.append(stack.pop())
    while stack1:
        p = stack1.pop()
        #print(p,c)
        COST[p-1] = min(c,COST[p-1])
        visited[p-1] = 1
        for pp in Edge[p-1]:
            if visited[pp-1]==0:
                stack.append(pp)
    c+=1
for c in range(len(COST)):
    if COST[c]==10000000:
        COST[c] = -1
    print(c+1, COST[c])
