# numbers = [1, 2, 3, 4, 5]

# for i in reversed(numbers):
#     print("첫 번쨰 반복문: {}".format(i))

# for i in reversed(numbers):
#     print("두 번쨰 반복문: {}".format(i))

# # 변수를 선언합니다.
# example_list = ["요소A", "요소B", "요소C"]

# # 그냥 출력합니다.
# print("# 단순 출력")
# print(example_list)
# print()

# # enumerate() 함수를 적용해 출력합니다.
# print("# enumberate() 함수 적용 출력")
# print(enumerate(example_list))
# print()

# # list() 함수로 강제 변환해 출력합니다.
# print("# list() 함수로 강제 변환 출력")
# print(list(enumerate(example_list)))
# print()

# # for 반복문과 enumerate() 함수 조합해서 사용하기
# print("# 반복문과 조합하기")
# for i, value in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(i, value))

# # 변수를 선언합니다.
# example_dictionary = {
#     "키A": "값A",
#     "키B": "값B",
#     "키C": "값C",
# }

# # 딕셔너리의 items() 함수 결과 출력하기
# print("# 딕셔너리의 items() 함수")
# print("items():", example_dictionary.items())
# print()

# # for 반복문과 items() 함수 조합해서 사용하기
# print("# 딕셔너리의 items() 함수와 반복문 조합하기")

# for key, element in example_dictionary.items():
#     print("dictionary[{}] = {}".format(key, element))

# # 리스트를 선언합니다.
# array = [i * i for i in range(1, 20, 2)]

# # 출력합니다.
# print(array)


# # 리스트를 선언합니다.
# array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]

# # 출력합니다.
# print(output)

# # 변수를 선언합니다.
# number = int(input("정수 입력> "))

# # if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print("\n".join(["입력한 문자열은 {}입니다.", "{}는(은) 짝수입니다."]).format(number, number))
# else:
#     print("\n".join(["입력한 문자열은 {}입니다.", "{}는(은) 홀수입니다."]).format(number, number))

# a = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
# counter = {}
# for i in a:
#     if i not in counter:
#         counter[i] = 0
#     counter[i] += 1

# print(f"{a}에서")
# print(f"사용된 숫자의 종류는 {len(counter)}개입니다.")
# print()
# print(f"참고: {counter}")

# from collections import Counter

# nucleos = input("염기 서열을 입력해주세요: ")
# counter = Counter(nucleos)

# for key in counter:
#     print(f"{key}의 개수: {counter[key]}")

# nucleos = input("염기 서열을 입력해주세요: ")
# counter = {}

# for i in range(0, len(nucleos), 3):
#     # 3글자씩 추출합니다.
#     codon = nucleos[i : i + 3]
#     # 3글자로 구성되는지 확인합니다.
#     if len(codon) == 3:
#         # 딕셔너리에 키가 없을 경우 추가합니다.
#         if codon not in counter:
#             counter[codon] = 0
#         # 갯수를 추가합니다.
#         counter[codon] += 1

# print(counter)

a = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
output = []

for i in a:
    if type(i) == list:
        # 요소가 리스트라면: 또 반복해서 요소를 추가합니다.
        for j in i:
            output.append(j)
    else:
        # 요소가 숫자라면: 그냥 추가합니다.
        output.append(i)

print(f"{a}를 평탄화하면")
print(f"{output}입니다")
