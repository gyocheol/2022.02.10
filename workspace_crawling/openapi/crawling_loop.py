from bs4 import BeautifulSoup
import requests


url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
# titles = soup.find_all('span', class_='title')
# print(titles)

# for title in titles:
#     print(title.text.strip())


updates = soup.find('nav', class_='pagination')
# print(updates)
# l = []
# for update in updates:
#     num = update.text
#     # print(num)
#     l.append(num)
#     lis = l[2:-2]
# print(lis)

# for update in updates:
#     # isdigit 찾아보기
#     if update.text.isdigit():
#         l.append(update.text)
# print(l)

# 한줄로 만들기
nums = list(filter(None, map(lambda x: x.text if x.text.isdigit() else None, updates)))
# print(nums)

sub_url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage='
for i in nums:
    soup = BeautifulSoup(requests.get(sub_url+i).text, 'html.parser')
    titles = soup.select('span[class=title]')
    for title in titles:
        print(title.text.strip())



