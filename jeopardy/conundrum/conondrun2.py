import requests

# URL del server
url = 'http://conundrum.challs.cyberchallenge.it/'

# Crea una sessione per gestire automaticamente i cookie
session = requests.Session()

# Prima, invia una richiesta GET per ottenere i cookie di sessione
response = session.get(url)

# Verifica che la richiesta sia stata correttamente eseguita
if response.status_code == 200:
    print("Risposta ricevuta dal server.")

    # Visualizza i cookie della sessione
    cookies = session.cookies.get_dict()
    print("Cookie della sessione:", cookies)

    # Verifica che il cookie "session" sia presente nei cookie
    if 'session' in cookies:
        session_cookie = cookies['session']
        print(f"Cookie di sessione recuperato: {session_cookie}")

        # Ora invia una richiesta POST al server per il calcolo del numero
        # Supponiamo che tu abbia già determinato il numero da inviare come 'guess'
        # In questo esempio, per semplicità, stiamo cercando di inviare il valore 'guess' con il valore corretto.
        guess = "1792"  # Esempio di numero da indovinare (questo dipenderà dall'indice di sessione)

        response_post = session.post(url + 'random', data=guess)

        if response_post.status_code == 200:
            print("Risultato della richiesta POST:", response_post.text)
        else:
            print("Errore nella richiesta POST:", response_post.status_code)
    else:
        print("Cookie di sessione non trovato.")
else:
    print(f"Errore nella richiesta GET: {response.status_code}")
