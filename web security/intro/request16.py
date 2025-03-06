import requests
from bs4 import BeautifulSoup

url='http://web-16.challs.olicyber.it/'

s=requests.get(url)

soup=BeautifulSoup(s.text,'html.parser')

pages = set()
new_pages = set([url])

while new_pages:
    current_pages = new_pages
    new_pages = set()
    for p in current_pages:
        print(f"Analysing {p}")
        try:
            s = requests.get(p)
            soup = BeautifulSoup(s.text, 'html.parser')
            for tag in soup.find_all(['a', 'h1']):
                if tag.name == 'a' and tag.has_attr('href'):
                    new_url = url + tag.get('href')
                    if new_url not in pages:
                        new_pages.add(new_url)
                        pages.add(new_url)
                if tag.name == 'h1' and 'flag{' in tag.text:
                    print(tag.text)
                    return 
        except requests.RequestException as e:
            print(f"Error fetching {p}: {e}")