# 에라토스테네스의 체

# 입력 받기
m, n = map(int, input().split())

# 소수를 저장하는 리스트
primes = []

# 2부터 n까지의 수를 모두 소수라 가정하고 시작
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

# m부터 n까지의 소수를 찾아서 출력
for num in range(max(2, m), n + 1):
    if is_prime[num]:
        primes.append(num)

# 결과 출력
for prime in primes:
    print(prime)

# 에라토스테네스의 체
# 이 알고리즘은 고대 그리스의 수학자 에라토스테네스에 의해 고안되었습니다.

# 알고리즘의 주요 아이디어는 다음과 같습니다:

# 2부터 시작하여, 현재까지 찾아낸 소수의 배수를 모두 제거한다.
# 남아 있는 가장 작은 수가 다음 소수이므로, 이를 찾아내고 해당 소수의 배수를 모두 제거한다.
# 반복하여 소수를 찾아내고, 남은 수가 없을 때까지 반복한다.

