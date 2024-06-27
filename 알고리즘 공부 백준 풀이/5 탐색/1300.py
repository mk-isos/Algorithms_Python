# 어렵다 완벽이해 x

# 문제 분석
# k는 min(10^9, N^2)이므로 시간 복잡도 N^2인 알고리즘 불가
# 이진 탐색으로 중앙값보다 작은 수의 개수를 세면서 범위를 절반씩 줄여서 B[k]값을 구함.

# 문제 풀이
# 2차원 리스트는 N행이 N의 배수로 구성
# 2차원 리스트에서 k번쨰 수는 k를 넘지 않음. 1~k번째 안에 답이 있음

# 시작 인덱스 1, 종료 인덱스를 k

# 중앙값보다 작은 수의 개수가 k보다 작으면 
# 시작 인덱스를 중앙값 + 1
# 중앙값보다 작은 수의 개수가 k보다 크거나 같으면
# 종료 인덱스를 중앙값 - 1 
# 정답을 중앙값으로 업뎃하면서 시작 인덱스가 종료 인덱스보다 커질 때까지 이진 탐색

N = int(input())
K = int(input())
start = 1
end = K
ans = 0
# 이진 탐색 수행
while start <= end:
    middle = int((start + end) / 2)
    cnt = 0
    # 중앙 값보다 작은 수 계산
    for i in range(1, N + 1):
        cnt += min(int(middle / i), N)  # 작은 수 카운트 핵심 로직
    if cnt < K:
        start = middle + 1
    else:
        ans = middle
        end = middle - 1
print(ans)
