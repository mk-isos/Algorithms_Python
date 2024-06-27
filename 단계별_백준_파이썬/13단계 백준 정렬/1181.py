N = int(input())

words = []

for _ in range(N):
    word = input().strip()
    words.append(word)

# 중복 제거 후 길이가 짧은 순서대로, 길이가 같으면 사전 순으로 정렬
sorted_words = sorted(set(words), key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)


# .strip(): 문자열의 양쪽 끝에 있는 공백을 제거
# sorted(set(words), key=lambda x: (len(x), x)): 정렬 함수인 sorted를 사용하여 중복이 제거된 단어들을 정렬합니다. 정렬할 때 사용되는 키(key) 함수는 lambda x: (len(x), x)로 정의되어 있습니다. 이 키 함수의 역할은 다음과 같습니다:

# len(x): 단어의 길이를 기준으로 정렬합니다. 길이가 짧은 순서대로 정렬됩니다.
# x: 길이가 같은 경우에는 단어 자체를 기준으로 정렬합니다. 이는 사전 순으로 정렬됩니다.