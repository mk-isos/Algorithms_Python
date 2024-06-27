def calculate_prize(dice):
    if len(set(dice)) == 1:
        return 10000 + dice[0] * 1000
    elif len(set(dice)) == 2:
        for num in dice:
            if dice.count(num) == 2:
                return 1000 + num * 100
    else:
        return max(dice) * 100

def main():
    # 참여하는 사람 수 입력
    n = int(input())
    
    max_prize = 0

    # 각 사람의 주사위 던진 결과 계산 및 최대 상금 갱신
    for _ in range(n):
        dice = list(map(int, input().split()))
        prize = calculate_prize(dice)
        max_prize = max(max_prize, prize)

    # 최대 상금 출력
    print(max_prize)

if __name__ == "__main__":
    main()
