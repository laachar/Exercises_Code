import requests

from bs4 import BeautifulSoup

URL ='https://www.amazon.com/Linux-Command-Line-2nd-Introduction/dp/1593279523/ref=sr_1_1?dchild=1&keywords=linux&qid=1631201714&rnid=2941120011&s=books&sr=1-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

