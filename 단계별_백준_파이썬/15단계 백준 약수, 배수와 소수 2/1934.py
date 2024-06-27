import math

# 최소공배수 계산하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

T = int(input())

# 각 테스트 케이스에 대해 최소공배수 계산 및 출력
for _ in range(T):
    A, B = map(int, input().split())
    result = lcm(A, B)
    print(result)
    
# 최대공약수만 구해도 최소공배수를 바로 알 수 있습니다.
# # 최소공배수 계산하는 함수
# def lcm(a, b):
#     return a * b // math.gcd(a, b)
