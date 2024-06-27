N, b = input().split()
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]  # N을 역순으로 바꿔줍니다.
result = 0

# N의 각 자리 숫자와 인덱스를 이용하여 결과를 계산합니다.
for i, n in enumerate(N):
    # result에 (b의 i제곱) * n에 해당하는 값을 더합니다.
    result += (int(b) ** i) * (num.index(n))
print(result)


# enumerate(N)은 주어진 iterable(여기서는 문자열 N)의 각 요소에 대해 인덱스와 값을 반환하는 파이썬 내장 함수입니다.

for i, n in enumerate(N):
    # i는 현재 요소의 인덱스, n은 현재 요소의 값
    # 이 부분에서 i는 N의 각 자리 숫자의 위치(인덱스), n은 해당 숫자 값
    result += (int(b) ** i) * (num.index(n))

# 여기서 enumerate(N)은 N의 각 자리 숫자에 대해 인덱스(i)와 값(n)을 제공합니다. 즉, for 루프에서 i는 현재 숫자의 위치(인덱스), n은 해당 숫자의 값이 됩니다. 이를 통해 코드는 N의 각 자리 숫자에 대해 적절한 계산을 수행하고 결과를 계산합니다.
