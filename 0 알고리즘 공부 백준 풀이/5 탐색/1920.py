# 문제 분석
# N의 최대 범위가 100,000 -? 단순 반복문으로 불가
# 이진 탐색 -> O(nlogn) 시간 복잡도로 해결
# 기본 정렬도 풀 수 있을 듯 근데 이진탐색 연습해볼래

# 문제 풀이
# 탐색 데이터를 1차원 리스트에 저장 후 정렬
# X라는 정수 존재를 이진 탐색을 사용

# if 중앙값 > target:
#     종료 인덱스 = 중간 인덱스 - 1
# elif 중앙값 < target:
#     시작 인덱스 = 중간 인덱스 + 1
# else:
#     찾았음, 반복문 종료

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    
    # 이진탐색 시작
    start = 0
    end = len(A) - 1
    
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    
    if find:
        print(1)
    else:
        print(0)
