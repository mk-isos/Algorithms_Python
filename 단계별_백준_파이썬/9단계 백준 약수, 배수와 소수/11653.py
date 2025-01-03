n = int(input())

if n == 1:
    print("")

# 2부터 하나씩 나눠보기
for i in range(2, n + 1):
    if n % i == 0:
        # 해당 숫자로 나눌 수 없을 때까지 나누기
        while n % i == 0:
            # 현재의 소인수를 출력하고 n을 해당 소인수로 나눔
            print(i)
            n = n / i


# 마지막으로, n = n / i는 현재 수(n)를 해당 소인수(i)로 나눈 결과를 다시 n에 할당하는 것입니다.
# 이렇게 함으로써 이미 찾아진 소인수로 나눈 값을 가지고 다음 소인수를 찾아나갑니다.


# 여기서 if는 숫자가 나눠질 수 있는지 판별하는 역할을 합니다.
# 찾아보니
# if 없이 while로만 해도 코드는 잘 돌아가지만 if가 있으면 코드가 빨리 돌아갑니다.

# 채점시간이 다른 문제들 보다 좀 오래걸리더라..
# 파이썬이 좀 오래걸리긴 하지만 다른 사람 풀이를 보니
N = int(input())


def question(N):
    while True:
        if N == 1:
            break
        else:
            for i in range(2, N + 1):
                if N % (i) == 0:
                    answer = i
                    break
            N = int(N / answer)
            print(answer)

    return 0


answer = question(N)

# 위처럼 푸니 2배이상 빨라졌다..
# 아래처럼 푸니 10배이상 빨라짐..
N = int(input())
N >= 1 and N <= 10000000


def insu(N):
    if N <= 1:
        return

    i = 2
    while i * i <= N:
        if N % i:
            i += 1
        else:
            N //= i
            print(i)

    if N > 1:
        print(N)


insu(N)

# 채점 현황 사진 업로드 어떰,,, 속도 비교

###### 코드 분석
# 첫 번째 코드:
# if n == 1: 구문을 통해 입력값이 1인 경우 아무것도 출력하지 않고 종료합니다.
# 소수인 경우에 해당하는 코드를 실행하며, 중첩된 while 루프를 통해 소인수를 찾고 출력합니다.

# 두 번째 코드:
# while True: 무한 루프를 통해 소인수를 찾고 출력하며, if N == 1: 구문을 통해 루프를 종료합니다.
# 입력값이 1인 경우에도 while 루프에 진입하므로 초기에 if N == 1: 구문이 조건을 만족하여 루프를 빠르게 종료합니다.

# 세 번째 코드:

# 입력값이 1인 경우 함수가 즉시 종료됩니다.
# while i * i <= N: 구문에서 루프가 sqrt(N) 번만 실행되기 때문에 전체적인 루프 횟수가 줄어들 수 있습니다.
# 나누어떨어지는지 여부를 확인하는 if N % i: 구문을 통해 조건이 참일 때 빠르게 루프를 탈출할 수 있습니다.


# 일반적으로 두 번째 코드와 세 번째 코드가 첫 번째 코드보다 빠른 이유는 다양합니다.
# 예를 들어, while 루프의 조건식, 루프 내부에서의 브레이크 조건, 변수의 활용 등이 코드 성능에 영향을 미칠 수 있습니다.
# 최적화된 코드는 입력 크기에 따라 더 효율적으로 동작할 수 있습니다.
# 하지만 파이썬의 경우 성능 차이가 그리 크지 않아서 작은 입력값에는 미미한 차이가 나타날 수 있습니다.
