# 문제 분석
# 예제 3번을 보면 단순한 방법으로 최대 공약수를 찾을 수 없다
# 규칙을 찾아보자면
# 수의 길이를 나타내는 두 수의 최대 공약수는 A와 B의 gcd 길이를 나타낸다.
# 
# 문제 풀이
# A B 의 최대 공약수를 유클리드 호제법을 이용해서 구하기
# 공약수 길이만큼 1 반복출력

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())

result = gcd(a, b)
while result > 0:
    print(1, end='')
    result -= 1
