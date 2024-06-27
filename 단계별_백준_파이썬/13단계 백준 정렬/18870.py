import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))  # 중복 제거 및 정렬


dic = {sorted_arr[i]: i for i in range(len(sorted_arr))}



for i in arr:
    print(dic[i], end=" ")


# dic = {sorted_arr[i]: i for i in range(len(sorted_arr))}
# 딕셔너리 dic를 생성합니다. 이 딕셔너리는 좌표를 압축하기 위해 사용됩니다.
# 딕셔너리의 키는 정렬된 좌표이고, 값은 해당 좌표의 압축된 인덱스입니다.

# 입력
# 5
# 2 4 -10 4 -9

# 출력
print(sorted_arr)   # [-10, -9, 2, 4]
print(dic)          # {-10: 0, -9: 1, 2: 2, 4: 3}

for i in arr:
    print(dic[i], end=" ")     # 2 3 0 3 1
