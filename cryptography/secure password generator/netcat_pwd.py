import socket
import time
import string
import random

HOST = "spg.challs.cyberchallenge.it"
PORT = 9600

# Genera un username casuale
def random_username(length=6):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Connessione al server e interazione con netcat
def interact():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.settimeout(2)  # Timeout per evitare blocchi

        def send_recv(data):
            s.sendall(data.encode() + b"\n")
            time.sleep(0.5)  # Aspetta un po' per la risposta
            return s.recv(1024).decode(errors="ignore")  # Riceve output

        output = s.recv(1024).decode(errors="ignore")  # Benvenuto
        print(output)

        passwords = []

        for _ in range(50):  # Registra 50 utenti
            username = random_username()
            print(f"[+] Registrando utente: {username}")

            send_recv("1")  # Sceglie "Register"
            output = send_recv(username)  # Manda il nome utente e riceve la password

            # Estrae la password cifrata
            lines = output.split("\n")
            for line in lines:
                if "Here is your super secure password:" in line:
                    password = line.split(": ")[1].strip()
                    passwords.append(password)
                    print(f"[+] Password ricevuta: {password}")

        print("\n--- PASSWORD RACCOLTE ---")
        for p in passwords:
            print(p)

        # Salva le password su un file
        with open("collected_passwords.txt", "w") as f:
            for p in passwords:
                f.write(p + "\n")

        print("[+] Password salvate in collected_passwords.txt")

if __name__ == "__main__":
    interact()
