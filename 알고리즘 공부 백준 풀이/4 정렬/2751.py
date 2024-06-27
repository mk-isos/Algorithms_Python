# 문제 분석
# N의 최대 범위 1,000,000 이므로 O(nlogn)의 시간복잡도로 정렬
# 병합 정렬 사용해본다

# 문제 풀이
# 정렬할 그룹을 최소 길이로 나누기
# 나눈 그룹마다 병합정렬
# ! 각 그룹마다 index 1, index 2를 지정해서 비교하면서 tmp배열에 병합 정렬
# 그 후 index 이동해서 다시 정렬

import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e - s < 1: return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)
    
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
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
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())
merge_sort(1, N)
for i in range(1, N + 1):
    print(str(A[i]) + '\n')
