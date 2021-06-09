import itertools
N_p = [i for i in range(int(input()))]
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

ans_s = 0
ans_c = 0
for l in itertools.permutations(N_p):
    print(l)
#print(ans_s,ans_c)
print(ans_s/ans_c)

