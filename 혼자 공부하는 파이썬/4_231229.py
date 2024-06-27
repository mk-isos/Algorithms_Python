# # 딕셔너리를 선언합니다.
# dicionaryionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀",
# }

# # 출력합니다.
# print("name:", dicionaryionary["name"])
# print("type:", dicionaryionary["type"])
# print("ingredient:", dicionaryionary["ingredient"])
# print("origin:", dicionaryionary["origin"])
# print()

# # 값을 변경합니다.
# dicionaryionary["name"] = "8D 건조 망고"
# print("name:", dicionaryionary["name"])

# print(dicionaryionary["ingredient"][0:2])

# dicionaryionary["client"] = "김문기"
# print(dicionaryionary["client"])
# print(dicionaryionary)

# #del dicionaryionary["client"]

# # 딕셔너리를 선언합니다.
# dicionaryionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀",
# }

# dicionaryionary["client"] = "김문기"
# # print(dicionaryionary["client"])
# # print(dicionaryionary)

# # 사용자로부터 입력을 받습니다.
# key = input("> 접근하고자 하는 키: ")

# # 출력합니다.
# if key in dicionaryionary:
#     print(dicionaryionary[key])
# else:
#     print("존재하지 않는 키에 접근하고 있습니다.")

# # 딕셔너리를 선언합니다.
# dictionary = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀",
#     "client": "킴문키",
#     "생일": "0316",
# }

# # for 반복문을 사용합니다.
# for key in dictionary:
#     # 출력합니다.
#     print(key, ":", dictionary[key])

# # 딕셔너리의 리스트를 선언합니다.
# pets = [
#     {"name": "구름", "age": 5},
#     {"name": "초코", "age": 3},
#     {"name": "아지", "age": 1},
#     {"name": "호랑이", "age": 1},
# ]

# print("# 우리 동네 애완 동물들")
# for key in pets:
#     print(key["name"], str(key["age"]) + "살")

# # 숫자는 무작위로 입력해도 상관 없습니다.
# numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] += 1
#     else:
#         counter[number] = 1

# # 최종 출력
# print(counter)


# # 딕셔너리를 선언합니다.
# character = {
#     "name": "기사",
#     "level": 12,
#     "items": {"sword": "불꽃의 검", "armor": "풀플레이트"},
#     "skill": ["베기", "세게 베기", "아주 세게 베기"],
# }

# # for 반복문을 사용하여 딕셔너리를 순회합니다.
# for key in character:
#     # 만약 값이 딕셔너리 형태라면
#     if type(character[key]) is dict:
#         # 중첩된 딕셔너리의 각 키와 값을 출력합니다.
#         for small_key in character[key]:
#             print(small_key, ":", character[key][small_key])
#     # 만약 값이 리스트 형태라면
#     elif type(character[key]) is list:
#         # 리스트의 각 아이템을 출력합니다.
#         for item in character[key]:
#             print(key, ":", item)
#     # 그 외의 경우에는 값 그대로를 출력합니다.
#     else:
#         print(key, ":", character[key])

# # 역반복문
# for i in range(4, 0 - 1, -1):
#     # 출력합니다.
#     print("현재 반복 변수: {}".format(i))

#############################################################
# output = ""

# for i in range(1, 10):
#     for j in range(0, i):
#         output += "*"
#     output += "\n"

# print(output)

# # 위에 꺼 간단하게
# output = ""

# for i in range(1, 10):
#     output += "*" * i
#     output += "\n"

# print(output)

##########################################################3
# output = ""

# for i in range(1, 15):
#     for j in range(14, i, -1):
#         output += " "
#     for k in range(0, 2 * i - 1):
#         output += "*"
#     output += "\n"

# print(output)

#########################################################

# # while 반복문을 사용합니다.
# while True:
#     # "."을 출력합니다.
#     # 기본적으로 end가 "\n"이라 줄바꿈이 일어나는데
#     # 빈 문자열 ""로 바꿔서 줄바꿈이 일어나지 않게 합니다.
#     print(".", end="")

# # 시간과 관련된 기능을 가져옵니다.
# import time

# # 변수를 선언합니다.
# number = 0

# # 5초 동안 반복합니다.
# target_tick = time.time() + 5
# while time.time() < target_tick:
#     number += 1

# # 출력합니다.
# print("5초 동안 {}번 반복했습니다.".format(number))

# limit = 5000
# i = 1

# # sum은 이미 파이썬 내부에서 사용하고 있는
# # 식별자이므로 sum_value라는 변수 이름을 사용했습니다.
# sum_value = 0
# while sum_value < limit:
#     sum_value += i
#     i += 1

# print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i - 1, limit, sum_value))

# # 리스트를 선언하고 뒤집습니다.
# list_a = [1, 2, 3, 4, 5]
# list_reversed = reversed(list_a)

# # 출력합니다.
# print("# reversed() 함수")
# print("reversed([1, 2, 3, 4, 5]):", list_reversed)
# print("list(reversed([1, 2, 3, 4, 5])):", list(list_reversed))
# print()

# # 반복문을 적용해 봅니다.
# print("# reversed() 함수와 반복문")
# print("for i in reversed([1, 2, 3, 4, 5]):")
# for i in reversed(list_a):
#     print("-", i)

# numbers = [1, 2, 3, 4, 5]

# for i in reversed(numbers):
#     print("첫 번쨰 반복문: {}".format(i))

# for i in reversed(numbers):
#     print("두 번쨰 반복문: {}".format(i))

temp = reversed([1, 2, 3, 4, 5])

for i in temp:
    print("첫 번쨰 반복문: {}".format(i))

for i in temp:
    print("두 번쨰 반복문: {}".format(i))
