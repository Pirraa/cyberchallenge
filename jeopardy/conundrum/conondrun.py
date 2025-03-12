import requests

# Array di numeri da provare
very_entropic_array = [
    1792, 1313, 3480, 1151, 1302, 1582, 9311, 3741, 1358, 1049,
    1254, 1732, 1289, 1524, 8608, 1986, 1289, 7144, 1585, 1487
]

# URL del server
url = 'http://conundrum.challs.cyberchallenge.it/random'

# Crea una sessione per gestire automaticamente i cookie
session = requests.Session()

# Fai una richiesta GET iniziale per ottenere il cookie di sessione
response = session.get('http://conundrum.challs.cyberchallenge.it/')
if response.status_code != 200:
    print(f"Errore nella richiesta GET iniziale: {response.status_code}")
    exit(1)

# Recupera il cookie della sessione
cookies = session.cookies.get_dict()
print("Cookie della sessione:", cookies)

# Cicla attraverso i numeri dell'array e invia una richiesta POST finché non trova la risposta con 'CCIT'
while True:
    for number in very_entropic_array:
        # Imposta il numero nel body della richiesta POST
        response_post = session.post(url, data=str(number))

        # Controlla se la risposta contiene "CCIT"
        if "CCIT" in response_post.text:
            print(f"Numero corretto trovato: {number}")
            print("Risposta:", response_post.text)
            exit(0)  # Esci quando trovi il numero corretto
        else:
            print(f"Prova con il numero {number}: non corretto.")
