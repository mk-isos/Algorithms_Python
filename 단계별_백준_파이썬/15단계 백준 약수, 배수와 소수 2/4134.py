# √N까지만 나눠서 소수를 판별하는 문제
#  n부터 시작해서 하나씩 증가시키면서 소수인지를 판별하고, 
# 소수일 경우 해당 값을 출력하고 반복문을 종료

# 브루트포스로 소수를 찾기

import math

# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    
    # n부터 시작해서 소수를 찾음
    while True:
        if is_prime(n):
            print(n)
            break
        n += 1

