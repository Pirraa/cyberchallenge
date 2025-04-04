from pwn import *
from string import printable

BLOCK_SIZE = 16
flag = ""

# Connessione aperta una sola volta
p = remote('ctf.unife.it', 8005)

def get_block(text, block_num=0):
    p.recvuntil(b"password to encrypt: ")
    p.sendline(text.encode())
    output = p.recvline().decode().strip()
    ct = output.split(": ")[1]
    return ct[block_num*32:(block_num+1)*32]

try:
    for i in range(1, 100):  # Tentiamo fino a 100 byte (in caso la flag sia lunga)
        pad_len = BLOCK_SIZE - (len(flag) % BLOCK_SIZE) - 1
        prefix = "A" * pad_len
        block_index = len(flag) // BLOCK_SIZE  # Quale blocco stiamo attaccando
        target_block = get_block(prefix, block_index)
        
        found = False
        for c in printable:
            guess = prefix + flag + c
            block = get_block(guess, block_index)
            if block == target_block:
                flag += c
                print(f"[+] Flag so far: {flag}")
                found = True
                break
        
        if not found:
            print("[!] Nessun carattere trovato, probabilmente fine della flag.")
            break

        if flag.endswith("}"):
            print("[✅] FLAG COMPLETA:", flag)
            break

finally:
    p.close()
