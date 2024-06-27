import sys

input = sys.stdin.readline

# 입력 받기
n = int(input())  # 상근이가 가지고 있는 숫자 카드의 개수
cards = set(map(int, input().split()))  # 숫자 카드에 적혀있는 정수들

m = int(input())  # 검사할 숫자의 개수
numbers_to_check = list(map(int, input().split()))  # 상근이가 가지고 있는지 검사할 숫자들

# 각 숫자가 상근이가 가지고 있는 숫자 카드에 적혀있는지 검사하여 결과 출력
result = [1 if num in cards else 0 for num in numbers_to_check]
print(' '.join(map(str, result)))

# result = [1 if num in cards else 0 for num in numbers_to_check] 
# 이 부분 연습

# import sys

# input = sys.stdin.readline

# 확실히 sys사용하면 좀 더 빨라진다.