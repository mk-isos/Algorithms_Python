# # 함수를 선언합니다.
# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# # 함수를 호출합니다.
# print("fibonacci(35):", fibonacci(35))
# print("fibonacci(50):", fibonacci(50))    #개오래 걸림


# # 변수를 선언합니다.
# counter = 0

# # 함수를 선언합니다.
# def fibonacci(n):
#     # 어떤 피보나치 수를 구하는지 출력합니다.
#     print("fibonacci({})를 구합니다.".format(n))
#     global counter
#     counter += 1
#     # 피보나치 수를 구합니다.
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # 함수를 호출합니다.
# fibonacci(10)
# print("---")
# print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))


# ##################

# # 메모 변수를 만듭니다.
# dictionary = {
#     1: 1,
#     2: 1
# }

# # 함수를 선언합니다.
# def fibonacci(n):
#     if n in dictionary:
#         # 메모가 되어 있으면 메모된 값을 리턴
#         return dictionary[n]
#     else:
#         # 메모가 되어 있지 않으면 값을 구함
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output

# # 함수를 호출합니다.
# print("fibonacci(10):", fibonacci(10))
# print("fibonacci(20):", fibonacci(20))
# print("fibonacci(30):", fibonacci(30))
# print("fibonacci(40):", fibonacci(40))
# print("fibonacci(50):", fibonacci(50))


# 랜덤한 숫자를 만들기 위해 가져옵니다.
import random

# 간단한 한글 리스트를 만듭니다.
hanguls = list("가나다라마바사아자차카타파하")

# 파일을 쓰기 모드로 엽니다.
with open("info.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        # 텍스트를 씁니다.
        file.write("{}, {}, {}\n".format(name, weight, height))
