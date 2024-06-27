#  2개의 for문을 이용해서 x, y 좌표로 주어지는 각 좌표의 숫자 리스트에서 개수가 한 개만 있는 숫자를 찾는 방법

x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)
