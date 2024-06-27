# # 3장 도전문제 1번
# import datetime

# 입력 = input("입력: ")

# if "안녕" in 입력:
#     print("안녕하세요.")
# elif "몇 시" in 입력:
#     now = datetime.datetime.now()
#     print(f"지금은 {now.hour}시입니다.")
# else:
#     print(입력)

# 3장 도전문제 2번
입력 = int(input("정수를 입력해주세요: "))

if 입력 % 2 == 0:
    print(f"{입력}은 2로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{입력}은 2로 나누어 떨어지는 숫자가 아닙니다.")

if 입력 % 3 == 0:
    print(f"{입력}은 3으로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{입력}은 3으로 나누어 떨어지는 숫자가 아닙니다.")

if 입력 % 4 == 0:
    print(f"{입력}은 4로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{입력}은 4로 나누어 떨어지는 숫자가 아닙니다.")

if 입력 % 5 == 0:
    print(f"{입력}은 5로 나누어 떨어지는 숫자입니다.")
else:
    print(f"{입력}은 5로 나누어 떨어지는 숫자가 아닙니다.")
