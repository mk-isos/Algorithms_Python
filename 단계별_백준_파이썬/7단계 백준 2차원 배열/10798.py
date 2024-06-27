# List = []
# for i in range(5):
#     a = input()
#     List.append(a)

# # 이렇게 고칠 수 있음
# # List = [input() for i in range(5)]

# for j in range(15):
#     for i in range(5):
#         if j < len(List[i]):
#             print(List[i][j], end="")

################ 정답

List = []

# 입력을 수집합니다.
for i in range(5):
    a = input()
    List.append(a)

# 문자를 세로로 출력합니다.
for j in range(max(len(word) for word in List)):
    for i in range(5):
        if j < len(List[i]):
            print(List[i][j], end="")

############# 정답 코드 주석 단 버전

# 빈 리스트를 생성합니다.
List = []

# 입력을 5번 수집합니다.
for i in range(5):
    a = input()
    List.append(a)

# 입력받은 문자열들을 세로로 출력합니다.
# 가장 긴 문자열의 길이를 기준으로 세로로 출력합니다.
for j in range(max(len(word) for word in List)):
    for i in range(5):
        # 현재 인덱스(j)가 문자열의 길이보다 작으면 해당 위치의 문자를 출력하고,
        # 그렇지 않으면 아무 것도 출력하지 않습니다.
        if j < len(List[i]):
            print(List[i][j], end="")


# 틀림/.............
# ##위에꺼 주석 단 버전

# # 빈 리스트를 생성합니다.
# List = []

# # 사용자로부터 5개의 단어를 입력받아 리스트에 추가합니다.
# for i in range(5):
#     a = input()
#     List.append(a)

# # 단어들을 세로로 출력합니다.
# # 각 단어의 길이를 기준으로 열의 높이를 설정하고,
# # 해당 열에서 각 단어의 문자를 출력합니다.
# for j in range(max(len(word) for word in List)):
#     for i in range(5):
#         # 현재 열의 인덱스가 해당 단어의 길이보다 작으면
#         # 해당 위치의 문자를 출력하고, 그렇지 않으면 공백을 출력합니다.
#         if j < len(List[i]):
#             print(List[i][j], end="")
#         else:
#             print(" ", end="")
