from sys import stdin
input = stdin.readline

x = input.rstrip()

## 1文字
# abc
s = input()

## n文字
# abc def ghi
a,b,c = input().split()
# リストに
str_list = list(input().split())  # n個の文字列がリストに格納される



## n数字
# 1 2 3
a,b,c = map(int, input().split())  # 3個の数字の入力を受け取る
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される


# n行1文字
#3
#aa
#a
#aaa
n = int(input())  # nは入力回数
str_list = [input() for _ in range(n)]

## n行1数字
#4
#2
#3
#4
#5
n = int(input())  # nは入力回数
num_list = [int(input()) for _ in range(n)]

# n行n文字
#3
#aaa b cc
#d ee fff
#gg hhh i

n = int(input())  # nは入力回数
str_list = []
for i in range(n):
    str_list.append(list(input().split()))
print(str_list)

#n行n数字
#3
#2 1 3
#3 1 2 3
#2 3 2

n = int(input())  # nは入力回数
num_list = [list(map(int, input().split())) for _ in range(n)]
print(num_list)



