import requests
from bs4 import BeautifulSoup

# URL della pagina da analizzare
url = 'http://web-15.challs.olicyber.it/'

# Scarica il contenuto della pagina
response = requests.get(url)
page_content = response.text

# Analizza il contenuto della pagina con BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')

# Trova tutte le risorse esterne (link, script, ecc.)
external_resources = []
for tag in soup.find_all(['link', 'script']):
    if tag.has_attr('href'):
        external_resources.append(tag['href'])
    elif tag.has_attr('src'):
        external_resources.append(tag['src'])

# Cerca la stringa 'flag{' nelle risorse esterne
for resource in external_resources:
    if not resource.startswith('http'):
        resource = url + resource
    try:
        resource_response = requests.get(resource)
        if 'flag{' in resource_response.text:
            print(f"Flag found in {resource}:")
            print(resource_response.text)
    except requests.RequestException as e:
        print(f"Error fetching {resource}: {e}")