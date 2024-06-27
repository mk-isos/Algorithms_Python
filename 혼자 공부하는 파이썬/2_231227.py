# # format() 함수로 숫자를 문자열로 변환하기
# string_a = "{}".format(10)

# # 출력하기
# print(string_a)
# print(type(string_a))

# # format() 함수로 숫자를 문자열로 변환하기
# format_a = "{}만 원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000)
# format_c = "{} {} {}".format(3000, 4000, 5000)
# format_d = "{} {} {}".format(1, "문자열", True)

# # 출력하기
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)

# # 정수
# output_a = "{:d}".format(52)

# # 특정 칸에 출력하기
# output_b = "{:5d}".format(52) # 5칸
# output_c = "{:10d}".format(52) # 10칸

# # 빈칸을 0으로 채우기
# output_d = "{:05d}".format(52) # 양수
# output_e = "{:05d}".format(-52) # 음수

# print("# 기본")
# print(output_a)
# print("# 특정 칸에 출력하기")
# print(output_b)
# print(output_c)
# print("# 빈칸을 0으로 채우기")
# print(output_d)
# print(output_e)

# # 조합하기
# output_h = "{:+5d}".format(52)  # 기호를 뒤로 밀기: 양수
# output_i = "{:+5d}".format(-52)  # 기호를 뒤로 밀기: 음수
# output_j = "{:=+5d}".format(52)  # 기호를 앞으로 밀기: 양수
# output_k = "{:=+5d}".format(-52)  # 기호를 앞으로 밀기: 음수
# output_l = "{:+05d}".format(52)  # 0으로 채우기: 양수
# output_m = "{:+05d}".format(-52)  # 0으로 채우기: 음수

# print("# 조합하기")
# print(output_h)
# print(output_i)
# print(output_j)
# print(output_k)
# print(output_l)
# print(output_m)

# # p.152 도전문제 1 : 구의 부피와 겉넓이
# pi = 3.141592
# r = float(input("구의 반지름을 입력해주세요: "))

# 부피 = (4 / 3) * pi * (r**3)
# 겉넓이 = 4 * pi * (r**2)
# print(f"= 구의 부피는 {부피}입니다.")
# print(f"= 구의 겉넓이는 {겉넓이}입니다.")

# # p.153 도전문제 2 : 피타고라스 정리

# a = float(input("밑변의 길이를 입력해주세요: "))
# b = float(input("높이의 길이를 입력해주세요: "))
# 빗변 = ((a**2) + (b**2)) ** (1 / 2)
# print(f"= 빗변의 길이는 {빗변}입니다. ")

# #답지 p.153 도전문제 2 : 피타고라스 정리
# 밑변 = float(input("밑변의 길이를 입력해주세요: "))
# 높이 = float(input("높이의 길이를 입력해주세요: "))ㅂㄴㅋㄴㅋ

# 빗변 = (밑변**2 + 높이**2) ** (1/2)

# print(f"= 빗변의 길이는 {빗변}입니다.")
