# 입력 받기
while True:
    n = int(input())
    if n == 0:
        break
    
    # 에라토스테네스의 체를 활용한 소수 판별
    is_prime = [True] * (2 * n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int((2 * n) ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, 2 * n + 1, i):
                is_prime[j] = False

    # 소수 개수 세기
    count = sum(1 for num in range(n + 1, 2 * n + 1) if is_prime[num])

    # 결과 출력
    print(count)


# 에라토스테네스의 체
# 이 알고리즘은 고대 그리스의 수학자 에라토스테네스에 의해 고안되었습니다.

# 알고리즘의 주요 아이디어는 다음과 같습니다:

# 2부터 시작하여, 현재까지 찾아낸 소수의 배수를 모두 제거한다.
# 남아 있는 가장 작은 수가 다음 소수이므로, 이를 찾아내고 해당 소수의 배수를 모두 제거한다.
# 반복하여 소수를 찾아내고, 남은 수가 없을 때까지 반복한다.
