# 학생들의 점수 입력 받기
scores = [int(input()) for _ in range(5)]

# 40점 이상인 경우는 그대로, 미만인 경우는 40점으로 변경
adjusted_scores = [max(score, 40) for score in scores]

# 평균 계산하여 출력
average_score = sum(adjusted_scores) // len(adjusted_scores)
print(average_score)
