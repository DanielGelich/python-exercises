import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
raw_html = r.text

soup = BeautifulSoup(raw_html, 'html.parser')
titles = soup.find_all('h2')

with open("hard-coded.txt", "w") as f:
    for title in titles:
        f.write(title.text.strip() + "\n")