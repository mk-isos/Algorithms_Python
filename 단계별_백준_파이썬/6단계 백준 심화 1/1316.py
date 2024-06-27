# n = int(input())
# group = 0

# for _ in range(n):
#     word = input()
#     error = 0
#     for i in range(len(word) - 1):  # 범위 0부터 단어개수 -1까지
#         if word[i] != word[i + 1]:  # 연속되는 두 문자가 다를 때
#             new_word = word[i + 1 :]  # 현재글자 이후 문자열을 새로운 단어로 생성
#             if new_word.count(word[i]) > 0:  # 남은 문자열에서 현재글자가 있있다면
#                 error += 1
#     if error == 0:
#             group += 1

# print(group)


n = int(input())
group = 0

for _ in range(n):
    word = input()
    error = 0
    for i in range(len(word) - 1):  # 범위 0부터 단어개수 -1까지
        if word[i] != word[i + 1]:  # 연속되는 두 문자가 다를 때
            new_word = word[i + 1 :]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[i]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1
    if error == 0:
        group += 1
print(group)




# error변수는 그룹 단어가 아닌 경우를 찾는 데 사용했다.
