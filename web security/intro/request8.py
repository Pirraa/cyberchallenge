import requests

url='http://web-08.challs.olicyber.it/login'

data={'username':'admin','password':'admin'}

response = requests.post(url, data=data)

if(response.status_code == 200):
    print(response.text)
else:
    print("Error: " + str(response.status_code) + " - " + str(response))