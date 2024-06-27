N, M = map(int, input().split())

# 집합 S 초기화
S = set()
for _ in range(N):
    string = input()
    S.add(string)

# 검사해야 하는 문자열 입력 및 검사
count = 0
for _ in range(M):
    test_string = input()
    if test_string in S:
        count += 1

print(count)
