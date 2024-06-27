# 문제 분석
# 그리디 방식
# 시간이 가장 적게 걸리는 사람 먼저 인출하도록 순서정하기!! -> 그리디
# N의 최대값이 1,000 그리고 시간제한 1초니까 n^2이하 알고리즘 아무거나 써서 정렬가능
# -> 삽입정렬 써봐야지.

# 문제 풀이
# 삽입 정렬 -> 오름차순 정렬
# 배열하고 합 배열 이용해서 계산.

# for j를 i-1~0까지 뒤에서부터 반복:
#     현재 범위에서 삽입 위치 찾기
# for j를 i~insert_point+1까지 뒤에서부터 반복:
#     삽입을 위해 삽입 위치에서 i까지 데이터를 한 칸씩 뒤로 밀기 
# 삽입 위치에 현재 데이터 저장

N = int(input())
A = list(map(int, input().split()))
S = [0]*N   # 합 배열

for i in range(1, N):    # 삽입 정렬
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, N):    # 합 배열 만들기
    S[i] = S[i-1] + A[i]
sum = 0

for i in range(0, N):    # 합 배열 총합 구하기
    sum += S[i]
print(sum)