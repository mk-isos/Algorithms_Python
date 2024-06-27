# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스에 대한 처리
for _ in range(T):
    yonsei_score = 0  # 연세대 득점 초기화
    korea_score = 0   # 고려대 득점 초기화
    
    # 9회 동안의 득점 입력 및 계산
    for _ in range(9):
        y, k = map(int, input().split())
        yonsei_score += y
        korea_score += k
    
    # 득점 비교하여 결과 출력
    if yonsei_score > korea_score:
        print("Yonsei")
    elif yonsei_score < korea_score:
        print("Korea")
    else:
        print("Draw")
