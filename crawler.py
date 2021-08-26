from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

naver = urlopen('https://naver.com')
naverHtml = naver.read()
naver.close()

naver_soup = soup(naverHtml, "html.parser")
print(naver_soup.h1)
