# 집합 A와 B의 원소의 개수 입력
n, m = map(int, input().split())

# 집합 A와 B의 원소 입력
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 대칭 차집합 계산
symmetric_difference = A.symmetric_difference(B)

# 대칭 차집합의 원소 개수 출력
print(len(symmetric_difference))


# symmetric_difference = A.symmetric_difference(B)
# 파이썬의 set 자료형에서 symmetric_difference 메서드는 두 집합의 대칭 차집합을 반환

# 처음에는 
# difference = (set_a - set_b).union(set_b - set_a)
# 이렇게 union 메서드를 이용
# union 메서드는 두 집합의 합집합을 반환