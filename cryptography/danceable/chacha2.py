from pwn import *
import random
import string

HOST = 'danceable.challs.cyberchallenge.it'
PORT = 9036

def generate_random_text(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    r = remote(HOST, PORT)
    
    # Attendi il messaggio iniziale completo
    print(r.recvuntil(b"> ").decode())  # Ricevi fino al prompt "> "

    
    # Invia "1" per cifrare
    r.sendline(b"1")
        
    # Attendi il prompt per l'input esadecimale
    print(r.recvuntil(b"hex)? ").decode())
        
    # Genera e invia un payload casuale
    plaintext = "a" * 16
    plaintext_hex = plaintext.encode().hex()
    r.sendline(plaintext_hex.encode())
        
    # Ricevi il ciphertext (assicurati di catturare tutta la linea)
    ciphertext = r.recvline().decode().strip()
    print(f"Plaintext: {plaintext} -> Ciphertext: {ciphertext}")
    keystream = xor(plaintext.encode(), bytes.fromhex(ciphertext)[:16])
    # Attendi il prossimo prompt "> "
    # 3. Estrai la flag (supponendo che sia nel blocco successivo)
    flag_ct = bytes.fromhex(ciphertext)[16:32]
    flag = xor(keystream, flag_ct)

    print("Flag:", flag.decode())
    print(r.recvuntil(b"> ").decode())

    r.close()

if __name__ == "__main__":
    main()