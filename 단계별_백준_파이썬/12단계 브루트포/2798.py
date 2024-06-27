n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = []

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = arr[i] + arr[j] + arr[k]
            if sum > m:
                continue
            else:
                res.append(sum)
print(max(res))

# 합이 M을 초과한다면 그냥 반복문을 계속 진행하고, M보다 작거나 같은 경우에는 그 값을 새로운 리스트에 추가

# ValueError: invalid literal for int() with base 10: '&' 
# 위 에러가 계속나서 해결법 찾아보다가 내가 문제인 점을 발견 못함.
# 그래서 그냥 로직 한번 더 확인하고 바로 채점돌리는데 그냥 맞았음.
# 그래서 다시 돌려보니 이번엔 오류 안뜨고 돌아감 뭘까 ...