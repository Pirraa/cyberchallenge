from pwn import *
from sympy import factorint, primerange
from math import gcd


def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

# === Funzione per mcd un numero ===
def diof(a,b,c):
    #equazione diofantea
    #soluzione equazione a*x+b*y=c
    g, x, y = egcd(a, b)
    if c % g != 0:
        return "impossible"
    else:
        x *= c // g
        y *= c // g
        return f"{x} {y}"


# === Connessione al servizio ===
HOST = 'ctf.unife.it'
PORT = 8013  # ⚠️ Cambia se necessario

p = remote(HOST, PORT)

# === Selezione della challenge "1) Factorization" ===
p.recvline()  # Legge la prima riga (benvenuto o simile)
p.recvline()  # Legge la seconda riga (menu o simile)
p.recvline()  # Legge la terza riga (menu o simile)
p.recvline()  # Legge la quarta riga (menu o simile)
p.recvline()  # Legge la quinta riga (menu o simile)
p.recvline()  # Legge la sesta riga (menu o simile)
p.sendline(b'3')
p.recvline()  # Legge la settima riga (menu o simile)

# === Risolviamo 5 challenge ===
for i in range(9):
    # Riceve il numero 
    line = p.recvline().decode().strip()
    print(f"[Challenge {i+1}] Domanda ricevuta:", line)

    # Estrai il numero dalla stringa
    try:
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        c = int(parts[2])
    except ValueError:
        # Cerca il numero nella stringa (es. "Fattorizza 12345")
        import re
        match = re.search(r'(\d+)', line)
        if match:
            number = int(match.group(1))
        else:
            print("[!] Errore: nessun numero trovato.")
            break

    #ottieni mdc dei numeri
    result=diof(a,b,c)

    # Invia la risposta
    p.sendline(str(result).encode())

    # Ricevi feedback ("Correct" o simile)
    #print("[*] Risposta del server:", p.recvline().decode().strip())
    # Assegna la risposta del server a una variabile
    server_response = p.recvline().decode().strip()
    print("[*] Risposta del server:", server_response)


# === Legge output finale (flag o messaggi) ===
try:
    while True:
        final_line = p.recvline(timeout=2).decode().strip()
        if not final_line:
            break
        print("[FLAG/MESSAGGIO] >", final_line)
except EOFError:
    print("[*] Connessione chiusa dal server.")