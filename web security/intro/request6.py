import requests

Session = requests.Session()
url = 'http://web-06.challs.olicyber.it/token'

response = Session.get(url)

url='http://web-06.challs.olicyber.it/flag'

response = Session.get(url)

if(response.status_code == 200):
    print(response.text)
else:
    print("Error: " + str(response.status_code) + " - " + response.text)