n = int(input())
result = 0
for i in range(1, n+1):
    
    nums = list(map(int, str(i))) # 198 -> [1,9,8]
    result = sum(nums) + i      # 18+ 198
    
    
    if result == n:         # 216 = 216
        print(i)        #198
        break
    if i == n:
        print(0)


######## 한번에 못 품 넘어려움 아니 걍 머리가 안돌아감


# nums = list(map(int, str(i))) 
# 파이썬에서 사용되는 리스트(list)와 맵(map) 함수를 활용

# 1 str(i): 정수 i를 문자열로 변환
# 2 map(int, ...): 문자열의 각 문자에 대해 int 함수를 적용하여 숫자로 변환
# list(...): 변환된 숫자들을 리스트로 