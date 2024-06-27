# 시간제한 2초,  N(1 ≤ N ≤ 10,000,000)
# 이런 상황에서는 O(nlogn)의 시간복잡도로 풀면 제한 시간을 초과
# 따라서 O(n)의 시간복잡도로 풀어야한다.

# 보통 이런 경우에 투 포인터르 사용한다고 한다.
#  투 포인터는 2개의 포인터로 알고리즘의 시간 복잡도를 최적화합니다.

# 이 문제는 연속된 자연수의 합을 구하는 것이므로 시작인덱스와 종료인덱스를 지정하여 연속된 수를 표현
# 시작 인덱스와 종료 인덱스를 투 포인터로 지정한 후에 문제 접근

# while end_index != n:
# if sum =n: 경우의 수 증가, end_index 증가, Sum값 변경
# elif sum 〉 n: Sum값 변경, start_index 증가
# else: end_index 증가, Sum값 변경

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)
