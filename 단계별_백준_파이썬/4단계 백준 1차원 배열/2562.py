L = []
for i in range(9):
    L.append(int(input()))  ## 리스트 안에 입력된 값들 차례대로 넣기

print(max(L))  ## max라는 메소드를 이용해 리스트 내의 최댓값 출력하기
print(L.index(max(L)) + 1)
