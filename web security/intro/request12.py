import requests
from bs4 import BeautifulSoup

url='http://web-12.challs.olicyber.it/'

response=requests.get(url)

soup=BeautifulSoup(response.text, 'html.parser')

print(soup.find_all('p')[1])