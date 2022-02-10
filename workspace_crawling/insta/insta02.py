from selenium import webdriver
from bs4 import BeautifulSoup


tag = input('search tags: ')
url = f'https://www.instagram.com/explore/tags/{tag}'

service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')

for img in img_list:
    print(img)

