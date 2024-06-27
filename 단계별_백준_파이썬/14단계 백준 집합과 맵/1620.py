# 포켓몬 도감 입력 받기
N, M = map(int, input().split())
pokemon_dict = {}  # 포켓몬 이름을 포켓몬 번호로 매핑하는 딕셔너리 생성
for i in range(1, N + 1):
    pokemon_name = input()
    pokemon_dict[pokemon_name] = i

# 문제 풀이
for _ in range(M):
    question = input()
    if question.isdigit():  # 입력이 숫자로만 이루어진 경우
        # 숫자에 해당하는 포켓몬 이름을 출력
        print(list(pokemon_dict.keys())[int(question) - 1])
    else:  # 입력이 알파벳으로만 이루어진 경우
        # 알파벳에 해당하는 포켓몬 번호를 출력
        print(pokemon_dict[question])

## 위 풀이 시간초과

######### 간단 풀이

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])