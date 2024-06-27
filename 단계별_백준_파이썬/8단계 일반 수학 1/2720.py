# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01

T = int(input())

for _ in range(T):
    C = int(input())
    for i in [25, 10, 5, 1]:
        print(C // i, end=" ")
        C = C % i

# 전형적인 그리디 알고리즘 문제
# 입력받는 돈에서 큰 화폐를 기준으로 나누고, 나눈 값은 출력하고 나머지 값은 다시 남은 돈으로 계산
