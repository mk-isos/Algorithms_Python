# Equilateral :  세 변의 길이가 모두 같은 경우  정삼각형
# Isosceles : 두 변의 길이만 같은 경우  이등변삼각형
# Scalene : 세 변의 길이가 모두 다른 경우   삼각형

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
