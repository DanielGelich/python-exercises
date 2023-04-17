import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

titles = soup.find_all('h2', class_='css-1qwxefa esl82me0')

for title in titles:
    print(title.text)