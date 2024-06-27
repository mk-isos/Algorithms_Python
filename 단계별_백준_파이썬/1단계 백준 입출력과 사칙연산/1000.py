# # 런타임에러 (ValueError)
# A = int(input(""))
# B = int(input(""))

# print("", A + B)


# # 다시
# A, B = input().split()  # 입력되는 문자를 input()함수로 입력받고 split()함수로 나누어 A,B 변수에 저장

# print(int(A) + int(B))  # int() 함수로 A와 B를 정수로 변환 하고 두수의 합을 출력


# map(int, input().split()): map 함수는 리스트의 각 요소에 int 함수를 적용하여
# 문자열의 리스트를 정수의 리스트로 변환합니다.
# 이 경우에는 ['5', '10']이 [5, 10]으로 변환됩니다.
a, b = map(int, input().split())
print(a + b)
