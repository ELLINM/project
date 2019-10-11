from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("https://movie.naver.com/movie/bi/mi/basic.nhn?code=167560")
soup = bs(html, "html.parser")
div = soup.find("div", {"class": "poster"})
img = div.find("img")
src = img.get("src")
print(src)
