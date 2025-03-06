import requests

# URL della risorsa
url = 'http://web-04.challs.olicyber.it/users'

# Richiesta senza specificare l'header Accept (default application/json)
response_default = requests.get(url)
print("Default response (application/json):")
print(response_default.text)

# Richiesta specificando l'header Accept come application/xml
headers = {'Accept': 'application/xml'}
response_xml = requests.get(url, headers=headers)
print("\nResponse with Accept: application/xml:")
print(response_xml.text)