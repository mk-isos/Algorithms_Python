# # from math import sin

# # print(sin(1))

# import random

# print("# random 모듈")

# # random(): 0.0 <= x < 1.0 사이의 float를 리턴합니다.
# print("- random():", random.random())

# # uniform(min, max): 지정한 범위 사이의 float를 리턴합니다.
# print("- uniform(10, 20):", random.uniform(10, 20))

# # randrange(): 지정한 범위의 int를 리턴합니다.
# # - randrange(max): 0부터 max 사이의 값을 리턴합니다.
# # - randrange(min, max): min부터 max 사이의 값을 리턴합니다.
# print("- randrange(10)", random.randrange(10))

# # choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
# print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

# # shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
# print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

# # sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
# print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))


# # 모듈을 읽어 들입니다.
# from urllib import request
# from bs4 import BeautifulSoup

# # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
# target = request.urlopen(
#     "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# )

# # BeautifulSoup을 사용해 웹 페이지를 분석합니다.
# soup = BeautifulSoup(target, "html.parser")

# # location 태그를 찾습니다.
# for location in soup.select("location"):
#     # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
#     print("도시:", location.select_one("city").string)
#     print("날씨:", location.select_one("wf").string)
#     print("최저기온:", location.select_one("tmn").string)
#     print("최고기온:", location.select_one("tmx").string)
#     print()

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "<h1>Hello World!</h1>"

# # 모듈을 읽어 들입니다.
# from flask import Flask
# from urllib import request
# from bs4 import BeautifulSoup

# # 웹 서버를 생성합니다.
# app = Flask(__name__)


# @app.route("/")
# def hello():
#     # urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
#     target = request.urlopen(
#         "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
#     )

#     # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
#     soup = BeautifulSoup(target, "html.parser")

#     # location 태그를 찾습니다.
#     output = ""
#     for location in soup.select("location"):
#         # 내부의 city, wf, tmn, tmx 태그를 찾아 출력합니다.
#         output += "<h3>{}</h3>".format(location.select_one("city").string)
#         output += "날씨: {}<br/>".format(location.select_one("wf").string)
#         output += "최저/최고 기온: {}/{}".format(
#             location.select_one("tmn").string, location.select_one("tmx").string
#         )
#         output += "<hr/>"
#     return output


# 함수 데코레이터를 생성합니다.
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")

    return wrapper


# 데코레이터를 붙여 함수를 만듭니다.
@test
def hello():
    print("hello")


# 함수를 호출합니다.
hello()
