from pwn import *
from sympy import factorint, primerange
from math import gcd

# === Funzione per mcd un numero ===
def mcd(a,b):
    # Se i numeri sono uguali, il mcd è il numero stesso
    if a == b:
        return a

    # Se uno dei numeri è zero, il mcd è l'altro numero
    if a == 0:
        return b
    if b == 0:
        return a

    # Calcola il mcd usando l'algoritmo di Euclide
    #divido a per b, calcolo resto a%b, sostituisco a con b e b con il resto, continuo finchè b non è 0
    #a,b=b,a%b assegno a il valore di b e b il resto della divisione
    while b != 0:
        a, b = b, a % b
    return a

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
p.sendline(b'2')
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
    divisor=mcd(a,b)

    # Invia la risposta
    p.sendline(str(divisor).encode())

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