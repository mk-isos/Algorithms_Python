# 크로아티아 알파벳

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in croatia:
    word = word.replace(i, "!")  # input 변수와 동일한 이름의 변수
print(len(word))


print(word)     #ljes=njak   ->   !e!!ak
