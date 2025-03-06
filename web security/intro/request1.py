import requests

res=requests.get(' http://web-01.challs.olicyber.it/')

if(res.status_code==200):
    print(res.text)
else:
    print("Error")
    