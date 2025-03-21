import socket
import time
import string
import random
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# === CONFIGURAZIONE ===
HOST = "spg.challs.cyberchallenge.it"
PORT = 9600
NUM_USERS = 200  # Numero di utenti da registrare

# === CHIAVE DES FISSA ===
KEY = b"\x00"*8  

# === FUNZIONE PER CIFRARE PASSWORD CON DES ECB ===
def encrypt_password(password):
    cipher = DES.new(KEY, DES.MODE_ECB)
    encrypted = cipher.encrypt(pad(password.encode(), 8))
    return encrypted.hex()[:12]  # Troncatura a 12 caratteri

# === GENERA UN USERNAME CASUALE ===
def random_username(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# === INTERAGISCE CON IL SERVER (netcat) ===
def interact():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.settimeout(1)

        def send_recv(data):
            s.sendall(data.encode() + b"\n")
            time.sleep(0.5)  # Aspetta la risposta
            return s.recv(1024).decode(errors="ignore")  # Riceve output

        output = s.recv(1024).decode(errors="ignore")  # Benvenuto
        print(output)

        passwords = []  # Password cifrate ottenute

        for _ in range(NUM_USERS):  # Registra più utenti
            username = random_username()
            print(f"[+] Registrando utente: {username}")

            send_recv("1")  # Sceglie "Register"
            output = send_recv(username)  # Manda il nome utente e riceve la password

            # Estrai la password cifrata
            lines = output.split("\n")
            for line in lines:
                if "Here is your super secure password:" in line:
                    password = line.split(": ")[1].strip()
                    passwords.append(password)
                    print(f"[+] Password ricevuta: {password}")

        # Salva le password su file
        with open("collected_passwords.txt", "w") as f:
            for p in passwords:
                f.write(p + "\n")

        print("[+] Password salvate in collected_passwords.txt")

        # === CONFRONTO CON WORDLIST ===
        match_passwords(s, passwords)

# === CONFRONTA PASSWORD CIFRATE CON WORDLIST E LOGGA ADMIN ===
def match_passwords(s, collected_passwords):
    print("\n[🔍] Inizio confronto con wordlist...\n")

    # Carica la wordlist e genera le versioni cifrate
    wordlist_file = "wordlist.txt"
    hashed_passwords = {}

    with open(wordlist_file, "r") as f:
        for line in f:
            password = line.strip()
            hashed = encrypt_password(password)
            hashed_passwords[hashed] = password  # Salviamo il mapping hash -> password

    # Controlliamo se una password cifrata dell'admin corrisponde a una parola della wordlist
    for hashed, password in hashed_passwords.items():
        if hashed in collected_passwords:
            print(f"🔑 [MATCH TROVATO] Password admin: {password}")
            login_as_admin(s, password)
            return  # Esci dopo il primo match

    print("❌ Nessuna corrispondenza trovata. Prova a raccogliere più password.")

# === TENTA IL LOGIN COME ADMIN CON LA PASSWORD TROVATA ===
def login_as_admin(s, password):
    print("\n[🔓] Tentativo di login come admin...")

    def send_recv(data):
        s.sendall(data.encode() + b"\n")
        time.sleep(0.5)
        return s.recv(1024).decode(errors="ignore")

    send_recv("2")  # Sceglie "Login"
    send_recv("admin")  # Inserisce "admin"
    response = send_recv(password)  # Inserisce la password
    print(response)
    #if "flag" in response.lower():
        #print("\n🎉 FLAG TROVATA! 🎉")
        #print(response)
    #else:
        #print("\n❌ Login fallito. Password sbagliata.")

# === ESEGUE LO SCRIPT PRINCIPALE ===
if __name__ == "__main__":
    interact()
