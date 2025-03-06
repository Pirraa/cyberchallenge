import requests

url = "http://web-03.challs.olicyber.it/flag"
headers = {
    "X-Password": "admin"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success! The response is:")
    print(response.text)
else:
    print(f"Failed to retrieve the resource. Status code: {response.status_code}")