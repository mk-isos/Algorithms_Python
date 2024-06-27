# def find_max_N(s):
#     total_sum = 0
#     n = 1

#     while total_sum + n <= s:
#         total_sum += n
#         n += 1

#     return n - 1


# # 입력 받기
# s = int(input())

# # 최댓값 찾기 및 출력
# result = find_max_N(s)
# print(result)


#########주석 버전
# find_max_N 함수 정의
def find_max_N(s):
    # 현재까지의 합을 저장하는 변수 초기화
    total_sum = 0
    # 서로 다른 자연수의 개수를 나타내는 변수 초기화
    n = 1

    # 합이 주어진 값 s를 초과하지 않는 선에서 반복
    while total_sum + n <= s:
        # 현재까지의 합에 n을 더함
        total_sum += n
        # 다음 자연수로 이동
        n += 1

    # 반복문을 빠져나왔을 때의 n-1 값이 최대 서로 다른 자연수의 개수
    return n - 1

# 입력 받기
s = int(input("자연수 S를 입력하세요: "))

# 최댓값 찾기 및 출력
result = find_max_N(s)
print("자연수 N의 최댓값은:", result)
