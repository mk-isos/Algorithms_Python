# 작은 두 변의 길이의 합이 제일 긴 변의 길이보다 커야 된다

num = sorted(map(int, input().split()))
res = num[0] + num[1] + min(num[2], num[0] + num[1] - 1)
print(res)

#  num[0]+num[1]-1, 1을 빼서 세 변의 길이 조건을 만족시키기 위한 보정
