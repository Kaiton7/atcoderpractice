from sys import stdin
input = stdin.readline
N = int(input())
S = input().rstrip()
one = [0 for i in range(10)]
two = [0 for i in range(100)]
three = [0 for i in range(1000)]

for s in S:
    for ix, el in enumerate(two):
        if two[ix]==1:
            three[int(str(ix)+s)] = 1
    for ix, el in enumerate(one):
        if one[ix]==1:
            two[int(str(ix)+s)] = 1
    one[int(s)] = 1
print(sum(three))