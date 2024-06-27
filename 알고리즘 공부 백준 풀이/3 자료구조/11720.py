# 파이썬의 리스트 자료구조로 쉽게 해결 가능.
# 주어진 숫자를 리스트의 형태로 저장한 뒤 리스트를 index를 이용해 탐색.
# 각 자릿수의 값을 정수형으로 변환해서 더하기.

n = input()
numbers = list(input())
sum = 0
for i in numbers:
    sum = sum + int(i)  # number에 있는 각 자리 수를 가져와 더해주기
print(sum)
