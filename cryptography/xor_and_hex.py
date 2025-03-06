#metodo one time pad: cifrare un messaggio facendo la xor tra il messaggio e la chiave
#se la chiave è corta posso decifrare il messaggio facendo la xor fra la chiave e il messaggio cifrato
#per fare la xor dato che è bit a bit il messaggio cifrato deve essere trasformato da esadecimale in byte con bytes.fromhex()
#la chiave è un byte quindi va da 0 a 255

import binascii

# Testo cifrato in esadecimale
ciphertext_hex = "104e137f425954137f74107f525511457f5468134d7f146c4c"
ciphertext_bytes = bytes.fromhex(ciphertext_hex)

# Tentiamo tutte le chiavi possibili (da 0x00 a 0xFF)
for key in range(256):
    plaintext_bytes = bytes(c ^ key for c in ciphertext_bytes)#xor equivalente alla funzione che ho messo nel file xorr
    try:
        plaintext = plaintext_bytes.decode()  # Proviamo a decodificare il testo
        if plaintext.isprintable():  # Controlliamo se è un testo leggibile
            print(f"Chiave: {key:02x} -> Testo decifrato: {plaintext}")
    except UnicodeDecodeError:
        continue
