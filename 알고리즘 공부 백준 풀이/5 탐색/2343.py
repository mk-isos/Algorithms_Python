# 완벽이해 X

# 문제 분석
# 블루레이의 크기가 모두 같고 녹화 순서가 바뀌지 않아야 함
# 이라는 조건에서 이진탐색을 떠올릴 수 있다
# 첫 레슨부터 마지막 레슨까지 저장하다 보면 지정한 블루레이 크기로 모든 레슨을 저장할 수 있는지 판단할 수 있으니
# 모두 저장할 수 있으면 블루레이 크기 줄이기
# 저장할 수 없으면 블루레이크기 늘리기
# 블루레이 최솟값 알 수 있음

# 문제 풀이
# 이진 탐색의 시작 인덱스는 최대 길이의 레슨
# 종료 인덱스는 모든 레슨 길이의 합
# 예시를 보면
# 시작 인덱스는 9, 종료 인덱스는 45
# 9~45 사이에서 이진 탐색 수행
# 중앙값 크기로 모든 레슨을 저장할 수 있으면
# 종료 인덱스 = 중앙값 - 1
# 중앙값 크기로 모든 레슨을 저장할 수 없으면
# 시작 인덱스 = 중앙값 + 1

N, M = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i  # 레슨 최댓값을 시작 인덱스로 저장
    end += i  # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    middle = int((start + end) / 2)
    sum = 0
    count = 0
    for i in range(N):  # 중간값으로 모든 레슨을 저장 할 수 있는지 확인
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)
