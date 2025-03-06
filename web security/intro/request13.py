import requests
from bs4 import BeautifulSoup

url='http://web-13.challs.olicyber.it/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

spans = soup.find_all('span')
for span in spans:
    print(span.get_text(), end='')