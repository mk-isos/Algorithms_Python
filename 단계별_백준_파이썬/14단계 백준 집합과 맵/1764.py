
# 듣도 못한 사람과 보도 못한 사람의 명단을 입력 받음
n, m = map(int, input().split())
not_heard = set(input() for _ in range(n))
not_seen = set(input() for _ in range(m))

# 듣보잡 명단 계산
intersection = not_heard.intersection(not_seen)
result = sorted(intersection)

# 듣보잡 수와 명단을 출력
print(len(result))
for name in result:
    print(name)


# intersection = not_heard.intersection(not_seen)
# 파이썬의 set 자료형에서 intersection 메서드는 두 집합 간의 공통된 원소를 포함한 새로운 집합을 반환

# 예를 들어, A 집합과 B 집합이 있을 때, A.intersection(B) 또는 B.intersection(A)는 A와 B의 교집합을 반환

