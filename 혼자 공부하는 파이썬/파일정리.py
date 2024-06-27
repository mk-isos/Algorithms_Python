# #
# # try except 구문을 사용합니다.
# try:
#     # 파일을 엽니다.
#     file = open("info.txt", "w")
#     # 여러 가지 처리를 수행합니다.
#     # 파일을 닫습니다.
#     file.close()
# except:
#     print("오류가 발생했습니다.")

# print("# 파일이 제대로 닫혔는지 확인하기")
# print("file.closed:", file.closed)

# #
# # try except 구문을 사용합니다.
# try:
#     # 파일을 엽니다.
#     file = open("info.txt", "w")
#     # 여러 가지 처리를 수행합니다.
#     예외.발생해라()
#     # 파일을 닫습니다.
#     file.close()
# except:
#     print("오류가 발생했습니다.")

# print("# 파일이 제대로 닫혔는지 확인하기")
# print("file.closed:", file.closed)

# #
# # try except 구문을 사용합니다.
# try:
#     # 파일을 엽니다.
#     file = open("info.txt", "w")
#     # 여러 가지 처리를 수행합니다.
#     예외.발생해라()
# except:
#     print("오류가 발생했습니다.")
# finally:
#     # 파일을 닫습니다.
#     file.close()

# print("# 파일이 제대로 닫혔는지 확인하기")
# print("file.closed:", file.closed)

# #
# # try except 구문을 사용합니다.
# try:
#     # 파일을 엽니다.
#     file = open("info.txt", "w")
#     # 여러 가지 처리를 수행합니다.
#     예외.발생해라()
# except:
#     print("오류가 발생했습니다.")

# # 파일을 닫습니다.
# file.close()
# print("# 파일이 제대로 닫혔는지 확인하기")
# print("file.closed:", file.closed)

# #
# # 파일을 엽니다.
# file = open("basic.txt", "w")
# # 파일에 텍스트를 씁니다.
# file.write("Hello Python Programming...!")

# # 파일을 닫습니다.
# file.close()

# #
# # 파일을 엽니다.
# with open("basic.txt", "r") as file:
#     # 파일을 읽고 출력합니다.
#     contents = file.read()
# print(contents)

# #
# with open("info.txt", "r") as file:
#     for line in file:
#         # 변수를 선언합니다.
#         (name, weight, height) = line.strip().split(", ")

#         # 데이터가 문제없는지 확인합니다: 문제가 있으면 지나감
#         if (not name) or (not weight) or (not height):
#             continue

#         # 결과를 계산합니다.
#         bmi = int(weight) / ((int(height) / 100) **2)
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else:
#             result = "저체중"

#         # 출력합니다.
#         print('\n'.join([
#             "이름: {}",
#             "몸무게: {}",
#             "키: {}",
#             "BMI: {}",
#             "결과: {}"
#         ]).format(name, weight, height, bmi, result))
#         print()
    

# #
# # 랜덤한 숫자를 만들기 위해 가져옵니다.
# import random
# # 간단한 한글 리스트를 만듭니다.
# hanguls = list("가나다라마바사아자차카타파하")
    
# # 파일을 쓰기 모드로 엽니다.
# with open("info.txt", "w") as file:
#     for i in range(1000):
#         # 랜덤한 값으로 변수를 생성합니다.
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)
#         # 텍스트를 씁니다.
#         file.write("{}, {}, {}\n".format(name, weight, height))
        

# #
