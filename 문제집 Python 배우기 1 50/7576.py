def calculate_height(bracelets):
    height = 10  # 처음에 그릇이 바닥에 놓인 상태의 높이
    for i in range(1, len(bracelets)):
        if bracelets[i] == bracelets[i-1]:
            height += 5  # 같은 방향으로 포개진 경우
        else:
            height += 10  # 반대 방향으로 쌓인 경우
    return height

# 입력 받기
bracelets = input()

# 최종 높이 계산 및 출력
result = calculate_height(bracelets)
print(result)


# calculate_height 함수:

# bracelets라는 문자열을 입력으로 받습니다. 이 문자열은 괄호로 표현된 그릇의 방향을 나타냅니다.
# height 변수를 10으로 초기화합니다. 이는 처음에 그릇이 바닥에 놓인 상태의 높이를 나타냅니다.
# 문자열을 순회하면서 각 그릇의 방향에 따라 높이를 더합니다.
# 만약 현재 그릇과 이전 그릇의 방향이 같다면 height에 5를 더합니다. (같은 방향으로 포개진 경우)
# 그렇지 않다면 height에 10을 더합니다. (반대 방향으로 쌓인 경우)
# 최종적으로 계산된 높이를 반환합니다.