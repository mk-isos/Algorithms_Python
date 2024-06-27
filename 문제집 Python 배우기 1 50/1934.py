#  최소공배수(LCM)

import math

# 최소공배수 계산하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 최소공배수 계산 및 출력
for _ in range(T):
    A, B = map(int, input().split())
    result = lcm(A, B)
    print(result)
