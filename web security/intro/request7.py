import requests

url = "http://web-07.challs.olicyber.it/"

response = requests.head(url)

print(f'status code: {response.status_code}')
# Print the headers
for header, value in response.headers.items():
    print(f"{header}: {value}")