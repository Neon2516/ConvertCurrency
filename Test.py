import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://cbr.ru/curreNcy_base/daily/")
html = BS(r.content, 'html.parser')

table1 = html.find('table')
headers = []
for i in table1.find_all('tr'):
    title = i.text.split("\n")[1:-1]
    headers.append(title)
for i in headers:
    if ('Доллар США' in i):
        print(i)
