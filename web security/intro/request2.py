import requests

res=requests.get('http://web-02.challs.olicyber.it/server-records',params={'id':'flag'})

if(res.status_code==200):
    print(res.text)
else:
    print("Error")
    print(res.status_code)