# def print_n_times(n, *values):
#     # n번 반복합니다.
#     for i in range(n):
#         # values는 리스트처럼 활용합니다.
#         for value in values:
#             print(value)
#         # 단순한 줄바꿈
#         print()


# # 함수를 호출합니다.
# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")


# # 함수를 선언합니다.
# def sum_all(start, end):
#     # 변수를 선언합니다.
#     output = 0
#     # 반복문을 돌려 숫자를 더합니다.
#     for i in range(start, end + 1):
#         output += i
#     # 리턴합니다.
#     return output


# # 함수를 호출합니다.
# print("0 to 100:", sum_all(0, 100))
# print("0 to 1000:", sum_all(0, 1000))
# print("50 to 100:", sum_all(50, 100))
# print("500 to 1000:", sum_all(500, 1000))


# 함수를 선언합니다.
def sum_all(start=0, end=100, step=1):
    # 변수를 선언합니다.
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1, step):
        output += i
    # 리턴합니다.
    return output


# 함수를 호출합니다.
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))
