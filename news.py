import requests
from bs4 import BeautifulSoup

url="https://news.ycombinator.com"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html.parser")

headlines=soup.find_all("span",class_="titleline")  ## it checks the news which has the name titleline and then it finds it
for i in headlines[:5]:
    print("\n",i.text)