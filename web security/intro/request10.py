import requests

url = 'http://web-10.challs.olicyber.it/'

# Determina i verbi supportati
response_options = requests.options(url)
supported_methods = response_options.headers.get('Allow', '').split(', ')

print(f"Supported methods: {supported_methods}")

# Prova a utilizzare un verbo meno comune, ad esempio HEAD
if  'PATCH' in supported_methods:
    print("PATCH method is supported.")
else:
    response_put = requests.patch(url)
    print(f"PATCH response status code: {response_put.status_code}")
    print(f"PATCH response body: {response_put.text}")
    print(f"PATCH response headers: {response_put.headers}")