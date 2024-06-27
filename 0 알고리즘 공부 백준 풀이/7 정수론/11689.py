# 문제 분석
# 자연수 n이 주어졌을 때, GCD(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램
# 이게 바로 오일러 피 함수의 정의 이다

# 문제 풀이
# 오일러 피 함수 구현하면 되겠지
# 링크 참고


import math
N = int(input())

result = N
for p in range(2, int(math.sqrt(N)) + 1):  # 제곱근까지만 진행
    if N % p == 0:  # p가 소인수인지 확인
        result -= result / p  # 결괏값 업데이트
        while N % p == 0:  # 2의 7승*11이라면 2의 7승을 없애고 11만 남김
            N /= p

if N > 1:  # 반복문에서 제곱근까지만 탐색했으므로 1개의 소인수가 누락되는 케이스 처리
    result -= result / N

print(int(result))
