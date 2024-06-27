# 문제 분석
# N의 최대 범위가 500,000이니까 O(nlogn) 시간복잡도로 정렬
# 병합 정렬로 정렬을 수행한 후 결과 출력

# 이 문제 제목이 버블 정렬인데 , N의 범위 때문에 버블 정렬 사용하면 시간 초과임.
# 그래서 병합정렬 사용합니당.
# 병합 정렬을 이해하셨다면 두 그룹을 병합하는 과정에서 버블 정렬의 swap이 포함되어 있다는 것을 아실거에요.

# 굿노트 사진 참고

# 위 사진 아이디어로 풀어봅니다.

# 문제 풀이
# 병합 정렬은 동일하게 진행.
# 정렬과정에서 index가 이동한 거리를 result에 저장할 거.

import sys
input = sys.stdin.readline
result = 0

def merge_sort(s, e):
    global result
    if e - s < 1: return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)  # 재귀 함수의 형태로 구현
    merge_sort(m + 1, e)
    
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:  # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k  # 뒤쪽 데이터 값이 더 작은 경우 결괏값 업데이트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * int(N + 1)
merge_sort(1, N)
print(result)
