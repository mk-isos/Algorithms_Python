N = input()

digits = [int(digit) for digit in str(N)]

sorted_digits = sorted(digits, reverse=True)

# 정렬된 자리수를 합쳐서 결과 출력
result = int("".join(map(str, sorted_digits)))  # 문자열들을join함수를 사용하여 하나의 문자열로
print(result)

# print(sorted_digits)     - > [4, 3, 2, 1]


# 간단한 예로 설명하면, 예를 들어 N이 2143일 경우:

# digits는 [2, 1, 4, 3]이 됩니다.
# sorted_digits는 [4, 3, 2, 1]이 됩니다.
# ''.join(map(str, sorted_digits))는 문자열 '4321'이 됩니다.
# result는 이 문자열을 정수로 변환한 4321이 됩니다.
