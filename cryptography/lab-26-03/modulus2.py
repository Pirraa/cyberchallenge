from pwn import *
from math import gcd
import sys

# Configurazione connessione
HOST = "ctf.unife.it"
PORT = 8015

# Funzione per calcolare n
def get_n():
    # Connetti al server
    r = remote(HOST, PORT)
    
    # Invia m=2 e ottieni c1
    r.recvuntil(b"Tell me a number\n")
    r.sendline(b"2")
    c1 = int(r.recvline().decode().strip())
    
    # Invia m=3 e ottieni c2
    r.recvuntil(b"Tell me another number\n")
    r.sendline(b"3")
    c2 = int(r.recvline().decode().strip())
    
    # Calcola n
    n = gcd(2**65537 - c1, 3**65537 - c2)
    
    # Invia n al server
    r.recvuntil(b"Tell me n\n")
    r.sendline(str(n).encode())
    
    # Stampa la risposta (flag)
    print(r.recvall().decode())
    
    r.close()

get_n()