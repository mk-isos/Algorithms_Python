# # 런타임에러
# for _ in range(100):
#     print(input())

#####
# 평소 입력값으로 몇번의 입력이 있는지 주어지는데 이번 문제같은 경우 몇번의 입력이 있었는지 전혀 정보가 주어지지 않아 try,except 구문을 통해 EOF에러발생시 break를 해줌으로써 해결하였다.


while True:
    try:
        print(input())
    except EOFError:
        break
