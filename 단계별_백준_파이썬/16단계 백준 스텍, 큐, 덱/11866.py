# 1 2 3 4 5 6 7
# 4 5 6 7 1 2           3
# 7 1 2 4 5             3 6
# 4 5 7 1               3 6 2
# . . .
#                       3 6 2 7 5 1 4

from collections import deque

n, k = map(int, input().split())

# 초기화된 원형 큐 생성
people = deque(range(1, n + 1))
result = []

while people:
    # k-1번째까지의 사람을 큐의 맨 뒤로 옮김
    for _ in range(k - 1):
        people.append(people.popleft())

    # k번째 사람을 제거하고 결과에 추가
    removed_person = people.popleft()
    result.append(removed_person)

print("<" + ", ".join(map(str, result)) + ">")

# print("<" + ", ".join(map(str, result)) + ">")
# 여러 요소를 콤마로 구분하여 문자열로 만들기