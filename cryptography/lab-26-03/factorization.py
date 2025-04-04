from pwn import *
from sympy import factorint, primerange
from math import gcd

# === Funzione per fattorizzare un numero ===
def trial_division_factorization(n):
    factors = []
    for p in primerange(2, int(n**0.5) + 1):
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    f = lambda x: (x * x + c) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d == n:
        return None  # Fail, riprova con altri parametri
    return d

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
p.sendline(b'1')
p.recvline()  # Legge la settima riga (menu o simile)

# === Risolviamo 5 challenge ===
for i in range(6):
    # Riceve il numero da fattorizzare
    line = p.recvline().decode().strip()
    print(f"[Challenge {i+1}] Domanda ricevuta:", line)

    # Estrai il numero dalla stringa
    try:
        number = int(line)
    except ValueError:
        # Cerca il numero nella stringa (es. "Fattorizza 12345")
        import re
        match = re.search(r'(\d+)', line)
        if match:
            number = int(match.group(1))
        else:
            print("[!] Errore: nessun numero trovato.")
            break

    # Fattorizza il numero
    #factors = trial_division_factorization(number)
    # Ottieni {fattore: esponente}
    factors = factorint(number)

    # Converti in lista (es: [p, q] se semiprimo)
    factor_list = []
    for base, exp in factors.items():
        factor_list.extend([base] * exp)
        answer = ' '.join(str(f) for f in factors)
    print(f" --> Risposta: {answer}")

    # Invia la risposta
    p.sendline(answer.encode())

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