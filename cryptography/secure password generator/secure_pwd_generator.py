import socket
import time
import string
import random

# === CONFIGURAZIONE SERVER ===
HOST = "spg.challs.cyberchallenge.it"
PORT = 9600
NUM_USERS = 200  # Numero di utenti da registrare

# === GENERA UN USERNAME CASUALE ===
def random_username(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# === INTERAGISCE CON IL SERVER (netcat) ===
def interact():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.settimeout(2)

        def send_recv(data):
            s.sendall(data.encode() + b"\n")
            time.sleep(0.5)  # Aspetta la risposta
            return s.recv(4096).decode(errors="ignore")  # Riceve output

        output = s.recv(4096).decode(errors="ignore")  # Benvenuto
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

        print("\n[✔] Raccolta password completata.")
        login_with_collected_passwords(s, passwords)

# === PROVA LE PASSWORD CIFRATE RACCOLTE NEL LOGIN ADMIN ===
def login_with_collected_passwords(s, collected_passwords):
    print("\n[🔍] Tentativo di login come admin con le password raccolte...\n")

    for password in collected_passwords:
        print(f"[*] Tentando login con: {password}")

        def send_recv(data):
            s.sendall(data.encode() + b"\n")
            time.sleep(0.5)
            return s.recv(4096).decode(errors="ignore")

        send_recv("2")  # Sceglie "Login"
        send_recv("admin")  # Inserisce "admin"
        response = send_recv(password)  # Inserisce la password cifrata

        #if "flag" in response.lower():
            #print("\n🎉 FLAG TROVATA! 🎉")
        print(response)
            #return  # Esci dopo aver trovato la flag

    print("\n❌ Nessuna password corretta trovata. Riprova creando più utenti.")

# === ESEGUE LO SCRIPT PRINCIPALE ===
if __name__ == "__main__":
    interact()
