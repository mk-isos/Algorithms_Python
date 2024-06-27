# n = int(input())

# a = n // 5
# b = a // 3

# if n % 5 == 0 & n % 3 == 0:
#     # print(a)
#     # print(b)
#     print(a + b)
# else:
#     print("-1")


###########3

# 출처 : https://puleugo.tistory.com/27

# 경우의 수는 총 4가지 입니다.

# N이 5로 나눠질 경우
# N이 5과 3의 조합으로 나눠 담을 수 있을 경우
# N이 3으로 나눠질 경우
# 그리고.. 5와 3으로는 나눠지지 않을 경우

#  최소한의 봉지만 사용하여 설탕을 담는 것이기 때문에

# 가장 큰 단위인 5만으로 나눠 담는 것
# 최소한의 3과 최대한의 5를 사용하여 나눠 담는 것
# 3으로 나눠 담는 것
# 나눠지지 않을 때

n = int(input())

if n % 5 == 0:  # 5으로 나눠떨어질 때
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif n == 0:  # 3으로 나눠떨어질 때
            print(p)
            break


