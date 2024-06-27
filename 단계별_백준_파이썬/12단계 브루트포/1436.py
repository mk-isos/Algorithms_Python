# N번째 종말의 수를 찾는 함수
def find_apocalypse_number(N):
    count = 0  # 찾은 종말의 수 개수
    num = 666  # 시작 수
    while True:
        if "666" in str(num):  # 만약 수에 '666'이 포함되어 있다면
            count += 1  # 종말의 수 개수를 증가시킴
            if count == N:  # N번째 종말의 수를 찾았다면 해당 수를 반환
                return num
        num += 1  # 다음 수로 넘어감

N = int(input())

result = find_apocalypse_number(N)
print(result)


#주의해야 할 점은 666, 1666, 2666, 3666, ... 형태로 증가 하지만 
# 5666 다음으로 큰 수들은 6660, 6661, 6662, ... 형태로 증가

# 코드가 매우 복잡 따라서  브루트 포스(Brute Force) 방법

