# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 양수 조건
# if number > 0:
#     print("양수입니다")

# # 음수 조건
# if number < 0:
#     print("음수입니다")

# # 0 조건
# if number == 0:
#     print("0입니다")

# # 날짜/시간과 관련된 기능을 가져옵니다.
# import datetime

# # 현재 날짜/시간을 구합니다.
# now = datetime.datetime.now()

# # 출력합니다.
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")

# # 출력합니다.
# print(
#     "{}년 {}월 {}일 {}시 {}분 {}초".format(
#         now.year, now.month, now.day, now.hour, now.minute, now.second
#     )
# )
# # 봄 구분
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다!".format(now.month))

# # 여름 구분
# if 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다!".format(now.month))

# # 가을 구분
# if 9 <= now.month <= 11:
#     print("이번 달은 {}월로 가을입니다!".format(now.month))

# # 겨울 구분
# if now.month == 12 or 1 <= now.month <= 2:
#     print("이번 달은 {}월로 겨울입니다!".format(now.month))

# # 입력을 받습니다.
# number = input("정수 입력> ")

# # 마지막 자리 숫자를 추출
# last_character = number[-1]

# # 숫자로 변환하기
# last_number = int(last_character)

# # 짝수 확인
# if (
#     last_number == 0
#     or last_number == 2
#     or last_number == 4
#     or last_number == 6
#     or last_number == 8
# ):
#     print("짝수입니다")

# # 홀수 확인
# if (
#     last_number == 1
#     or last_number == 3
#     or last_number == 5
#     or last_number == 7
#     or last_number == 9
# ):
#     print("홀수입니다")

# # 입력을 받습니다.
# number = input("정수 입력> ")
# last_character = number[-1]

# # 짝수 조건
# if last_character in "02468":
#     print("짝수입니다")

# # 홀수 조건
# if last_character in "13579":
#     print("홀수입니다")

# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 짝수 조건
# if number % 2 == 0:
#     print("짝수입니다")

# # 홀수 조건
# if number % 2 == 1:
#     print("홀수입니다")

# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 조건문을 사용합니다.
# if number % 2 == 0:
#     # 조건이 참일 때, 즉 짝수 조건
#     print("짝수입니다")
# else:
#     # 조건이 거짓일 때, 즉 홀수 조건
#     print("홀수입니다")

# # 변수를 선언합니다.
# score = float(input("학점 입력> "))

# # 조건문을 적용합니다.
# if score == 4.5:
#     print("신")
# elif 4.2 <= score:
#     print("교수님의 사랑")
# elif 3.5 <= score:
#     print("현 체제의 수호자")
# elif 2.8 <= score:
#     print("일반인")
# elif 2.3 <= score:
#     print("일탈을 꿈꾸는 소시민")
# elif 1.75 <= score:
#     print("오락문화의 선구자")
# elif 1.0 <= score:
#     print("불가촉천민")
# elif 0.5 <= score:
#     print("자벌레")
# elif 0 < score:
#     print("플랑크톤")
# else:
#     print("시대를 앞서가는 혁명의 씨앗")

# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 조건문 사용
# if number > 0:
#     # 양수일 때: 아직 미구현 상태입니다.
#     pass
# else:
#     # 음수일 때: 아직 미구현 상태입니다.
#     pass

# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# # 조건문 사용
# if number > 0:
#     # 양수일 때: 아직 미구현 상태입니다.
#     raise NotImplementedError
# else:
#     # 음수일 때: 아직 미구현 상태입니다.
#     raise NotImplementedError

# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)

# if 10 < number < 20:
#     print("조건 충족")
