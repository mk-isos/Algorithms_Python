# 모든 점수 입력 받고, 최고점 별도로 저장 해놓기
# 점수를 A, B, C 받는다 치면
# (A/M*100 + B/M*100 + C/M*100) / 3 으로 나누는 것인데
# 최종적으로 (A+B+C) * 100 / M / 3 을 계싼하면 되겠다.
# 최종 식 : 총합 * 100 / M / 3

n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)
# 한 과목과 관련된 수식을 총합한 후 관련된 수식으로 변환해 로직이 간단해짐
print(sum * 100 / mymax / int(n))
