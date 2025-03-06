import requests

url='http://web-11.challs.olicyber.it/login'
url2='http://web-11.challs.olicyber.it/flag_piece'

data = {
    'username': 'admin',
    'password': 'admin'
}
flag=''
token=''


with requests.Session() as session:
    for i in range(4):
        response = session.post(url, json=data)

        if response.status_code == 200:
            print(response.cookies)
            print(response.json())
            token = response.json()['csrf']
        else:
            print('Error:', response.status_code)
            print(response.text)

        response2 = session.get(url2,  params={'index': i, 'csrf': token})
        if response2.status_code == 200:
            print(response2.json())
            flag += response2.json()['flag_piece']
        else:
            print('Error:', response2.status_code)
            print(response2.text)

print(flag)