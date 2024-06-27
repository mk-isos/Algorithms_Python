# 문제 분석
# 전형적인 그리디 알고리즘
# 뒤의 동전 Ai가 앞에 나오는 동전 Ai-1의 배수가 된다는 조건
# 즉 가격이 큰 동전 먼저 사용하면 되는거임

N, K = map(int, input().split())
A = [0] * N
for i in range(N):
    A[i] = int(input())
count = 0
for i in range(N - 1, -1, -1):
    if A[i] <= K:  # 현재 동전의 가치가 K보다 작거나 같으면 구성에 추가
        count += int(K / A[i])
        K = K % A[i]  # K를 현재 동전을 사용하고 남은 금액으로 갱신
print(count)
