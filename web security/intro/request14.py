from bs4 import BeautifulSoup, Comment

import requests

resp=requests.get('http://web-14.challs.olicyber.it/')
html_doc=resp.text
soup = BeautifulSoup(html_doc, 'html.parser')

# Trova tutti i commenti nel documento
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

for comment in comments:
    print(comment)