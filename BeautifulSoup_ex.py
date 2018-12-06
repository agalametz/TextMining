from bs4 import BeautifulSoup
import requests
url = 'http://www.audreygalametz.com/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)
print(soup.title)
print(soup.get_text())
