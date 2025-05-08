from pwn import *

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def main():
    # Connessione al server
    r = remote('danceable.challs.cyberchallenge.it', 9036)
    
    # Attendi il menu iniziale
    r.recvuntil(b"> ")
    
    # Fase 1: Ottenere il keystream con un plaintext noto (16 byte)
    plaintext = b"a" * 16
    r.sendline(b"1")
    r.recvuntil(b"hex)? ")
    r.sendline(plaintext.hex().encode())
    
    # Ricevi il ciphertext completo
    ciphertext = bytes.fromhex(r.recvline().strip().decode())
    
    # Calcola il keystream (primi 16 byte)
    keystream = xor(plaintext, ciphertext[:16])
    
    # Fase 2: Estrai la flag dai blocchi successivi
    flag_blocks = []
    for i in range(16, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        flag_block = xor(keystream, block)
        flag_blocks.append(flag_block)
    
    # Combina tutti i blocchi della flag
    full_flag = b"".join(flag_blocks)
    
    # Trova la flag nel risultato (cerca il pattern CCIT{...})
    try:
        start = full_flag.index(b"CCIT{")
        end = full_flag.index(b"}", start) + 1
        clean_flag = full_flag[start:end].decode()
    except (ValueError, UnicodeDecodeError):
        # Fallback: stampa in esadecimale se la decodifica fallisce
        print("Flag (hex):", full_flag.hex())
        clean_flag = None
    
    if clean_flag:
        print("Flag trovata:", clean_flag)
    else:
        print("Impossibile decodificare la flag come testo, vedi output esadecimale sopra")
    
    r.close()

if __name__ == "__main__":
    main()