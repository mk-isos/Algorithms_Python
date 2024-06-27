# 연립방정식

#######연방 풀이


a, b, c, d, e, f = map(int, input().split())

print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))

###### 브루트 포스

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)
            

# 다시 풀기 블로그 참고 함 위 풀이는