# 나눗셈의 나머지와 몫을 활용하는 문제

h,m,s = map(int,input().split())
t = int(input())

s += t
m += s//60
h += m//60
print(h%24,m%60,s%60)