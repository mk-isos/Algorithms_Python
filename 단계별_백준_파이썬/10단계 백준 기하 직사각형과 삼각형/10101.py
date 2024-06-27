# 세 각의 크기가 모두 60이면, Equilateral 정삼각형
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles 이등변 삼각형
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene 삼각형?
# 세 각의 합이 180이 아닌 경우에는 Error 삼각형 x


t = [int(input()) for i in range(3)]
if t.count(60) == 3:
    print("Equilateral")
elif sum(t) == 180 and len(set(t)) == 2:  # set은 집합 자료형인데 중복을 허용하지 않음
    print("Isosceles")
elif sum(t) == 180 and len(set(t)) == 3:
    print("Scalene")
else:
    print("Error")


# set은 집합 자료형인데 중복을 허용하지 않음
