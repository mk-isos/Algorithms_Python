n = input()

print(sum(map(int, input())))  # sum함수를 이용


## 2 방법 for 문
n = int(input())
nums = input()
total = 0
for i in range(n):  # 0부터 n-1까지
    total += int(nums[i])
print(total)
