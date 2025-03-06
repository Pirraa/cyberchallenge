import requests
from bs4 import BeautifulSoup

base_url = "http://web-16.challs.olicyber.it/"
visited = set()

def find_flag(url):
    if url in visited:
        return None
    visited.add(url)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Check if the flag is in the <h1> tag
    h1_tag = soup.find('h1')
    if h1_tag and 'flag' in h1_tag.text:
        return h1_tag.text

    # Find all links and traverse them
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/'):
            full_url = base_url + href.lstrip('/')
            flag = find_flag(full_url)
            if flag:
                return flag

    return None

flag = find_flag(base_url)
if flag:
    print("Flag found:", flag)
else:
    print("Flag not found")