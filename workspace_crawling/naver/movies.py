from bs4 import BeautifulSoup
import urllib.request


# 해당 url에 요청, 서버가 응답
resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver#')
# resp에는 doc이 들어있다!
# print(resp)
# 응답된 문서를 파이썬이 가지고 있는 내장 parer를 이용해서 parser tree(노드 구조)를 만들어 줌
soup = BeautifulSoup(resp, 'html.parser')
# 객체!!
# print(type(soup))

# 제목과 별점 가져오기
movies = soup.find_all('dl', class_='lst_dsc')
# print(movies[0])
for movie in movies:
    # 제목 / .get_text() 대신 .string, .text 가능
    title = movie.find('a').get_text()

    # 별점
    star = movie.find('span', class_= 'num').text

    print(f'{title} [{star}]')
