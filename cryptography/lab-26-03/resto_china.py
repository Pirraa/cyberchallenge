from functools import reduce
from pwn import *
from sympy import factorint, primerange
from math import gcd



def chinese_remainder_theorem(a, M):
    # Calcola il prodotto di tutti i moduli
    F = reduce(lambda x, y: x * y, M)

    # Calcola la soluzione usando il teorema cinese del resto
    x = 0
    for ai, Mi in zip(a, M):
        Mi_ = F // Mi
        # Calcola l'inverso moltiplicativo di Mi_ modulo Mi
        Mi_inv = pow(Mi_, -1, Mi)
        x += ai * Mi_ * Mi_inv

    # Riduci x modulo F per ottenere la soluzione minima
    x %= F
    return x, F

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
p.sendline(b'4')
p.recvline()  # Legge la settima riga (menu o simile)

# === Risolviamo 5 challenge ===
for i in range(9):
    # Riceve il numero 
    line = p.recvline().decode().strip()
    print(f"[Challenge {i+1}] Domanda ricevuta:", line)

    # Estrai il numero dalla stringa
    try:
        # Converti line in intero
        n = int(line)

        # Inizializza i vettori
        a = []
        M = []

        # Ciclo per leggere coppie di interi
        for _ in range(n):
            pair_line = p.recvline().decode().strip()
            pair = list(map(int, pair_line.split()))
            if len(pair) == 2:
                a.append(pair[0])
                M.append(pair[1])
            else:
                print("[!] Errore: coppia non valida.")
                break
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
    result=chinese_remainder_theorem(a,M)
    print(result)
    # Invia il risultato al server
    p.sendline(f"{result[0]} {result[1]}".encode())


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