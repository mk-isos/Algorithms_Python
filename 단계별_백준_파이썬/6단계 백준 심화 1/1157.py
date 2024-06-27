# 이해가 조금 어려웠음
# 한번 더 공부하기가 필요하다.

words = input().upper()   #upper 함수를 이용하여 문자열을 모두 대문자로 변환하고서 words
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거
                                # 문자열 중 중복되는 요소는 set함수를 이용해서 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 추가

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])
    
    