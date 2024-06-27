
N = int(input())
N_L = [*map(int, input().split())]
M = int(input())
M_L = [*map(int, input().split())]


count = {}      # 빈 딕셔너리인 count를 초기화
for num in N_L:
    if num in count:
        count[num] += 1 # 이미 딕셔너리에 있는 숫자라면 해당 숫자의 등장 횟수를 1 증가
    else:
        count[num] = 1  # 그렇지 않다면 해당 숫자를 딕셔너리에 추가하고 등장 횟수를 1

for target in M_L:
    result = count.get(target)  # target에 해당하는 값(등장 횟수)을 가져오기
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")


# N = int(input())
# N_L = [*map(int, input().split())]
# M = int(input())
# M_L = [*map(int, input().split())]

# 여기서 *는 map 함수의 결과를 리스트로 언패킹하는 역할
# map 함수의 결과를 리스트로 변환하는데, *가 이 역할을 한다.

# 예를 들어, 사용자가 "1 2 3"을 입력했다면, 
# input().split()은 ['1', '2', '3']을 반환하고, 
# map(int, input().split())은 (1, 2, 3)을 반환합니다. 
# 마지막으로, [*map(int, input().split())]은 [1, 2, 3]으로 변환됩니다.

