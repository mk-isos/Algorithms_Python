# 입력 받기
n = int(input())
logs = []

for _ in range(n):
    logs.append(input().split())

# 출입 기록을 저장할 딕셔너리
status = {}

# 출입 기록 처리
for log in logs:
    name, action = log[0], log[1]

    if action == "enter":
        status[name] = True  # 출근 상태로 업데이트
    else:
        status[name] = False  # 퇴근 상태로 업데이트

#####################
# 현재 회사에 있는 사람들을 사전 순의 역순으로 출력
for name, is_present in sorted(status.items(), key=lambda x: x[0], reverse=True):
    if is_present:
        print(name)

# items() 함수는 딕셔너리의 키-값 쌍을 튜플로 반환하고,
# key=lambda x: x[0]는 튜플의 첫 번째 요소인 이름을 기준으로 정렬


# for name, is_present in sorted(status.items(), key=lambda x: x[0], reverse=True):
#     if is_present:
#         print(name)

# items() 함수는 딕셔너리의 키-값 쌍을 튜플로 반환하고,
# key=lambda x: x[0]는 튜플의 첫 번째 요소인 이름을 기준으로 정렬